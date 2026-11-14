import re
from knowledge_graph import (
    NODES,
    ALIASES,
    EDUCATIONAL_CONTENT,
    get_domain_members,
    get_topic_domains,
    get_prerequisites,
    get_next_topics,
    get_related_topics,
    bfs_path,
)


def find_entities(question):
    """Find graph entities mentioned in a question, ordered by appearance."""
    q = question.lower()
    found_positions = []

    # Check longer aliases first so 'linear algebra' matches before shorter terms.
    candidates = sorted(ALIASES.items(), key=lambda item: len(item[0]), reverse=True)
    for alias, canonical in candidates:
        pattern = r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])"
        match = re.search(pattern, q)
        if match:
            found_positions.append((match.start(), canonical))

    for node in sorted(NODES, key=len, reverse=True):
        pattern = r"(?<![a-z0-9])" + re.escape(node.lower()) + r"(?![a-z0-9])"
        match = re.search(pattern, q)
        if match:
            found_positions.append((match.start(), node))

    # Sort by position in the sentence and deduplicate while preserving order.
    found_positions.sort(key=lambda item: item[0])
    matches = []
    for _, canonical in found_positions:
        if canonical not in matches:
            matches.append(canonical)

    return matches


def format_list(items):
    if not items:
        return "None recorded."
    return ", ".join(items) + "."


def answer_question(question):
    q = question.lower().strip()
    entities = find_entities(question)

    if not entities:
        return (
            "I couldn't identify a topic from the current knowledge graph. "
            "Try asking about Programming in C, Data Structures, Algorithms, "
            "Machine Learning, Probability, Linear Algebra, DBMS, Operating Systems, "
            "Computer Networks, Digital Logic, or Computer Architecture."
        )

    # 1. PATH (BFS-based connection between two topics)
    if len(entities) >= 2 and any(
        word in q for word in ["path", "route", "how to reach", "connection", "connected", "between", "to"]
    ):
        start, target = entities[0], entities[1]
        path = bfs_path(start, target)
        if path:
            return (
                f"Shortest prerequisite path (BFS): {' → '.join(path)} "
                f"({len(path) - 1} edge{'s' if len(path) - 1 != 1 else ''})."
            )
        return f"No directed prerequisite path was found from {start} to {target}."

    topic = entities[0]
    info = EDUCATIONAL_CONTENT.get(topic, {})

    # 2. DEFINITION (Explanation of the topic)
    if any(
        word in q for word in ["define", "definition", "what is", "what are", "explain", "meaning of", "overview"]
    ):
        # Avoid catching "what are the prerequisites..." or "what are the examples..."
        if not any(k in q for k in ["prerequisite", "example", "domain", "belong", "related", "prepare", "roadmap"]):
            definition = info.get("definition", f"{topic} is a concept in the CSE Knowledge Graph.")
            domains = get_topic_domains(topic)
            domain_note = f" (Domain: {', '.join(domains)})" if domains else ""
            return f"{topic}{domain_note}: {definition}"

    # 3. PREPARATION (Step-by-step learning roadmap)
    if any(
        word in q for word in ["prepare", "preparation", "roadmap", "how to learn", "how to study", "steps to learn", "study plan"]
    ):
        prereqs = get_prerequisites(topic)
        roadmap = info.get("roadmap", [])
        lines = [f"Preparation Roadmap for {topic}:"]
        if prereqs:
            lines.append(f"• Graph Prerequisites to cover first: {', '.join(prereqs)}")
        for idx, step in enumerate(roadmap, start=1):
            lines.append(f"{idx}. {step}")
        return "\n".join(lines)

    # 4. PREREQUISITES (Topics to learn first)
    if any(
        word in q for word in ["prerequisite", "before", "required for", "learn first", "need to know"]
    ):
        target = entities[-1]
        prerequisites = get_prerequisites(target)
        if prerequisites:
            return f"Prerequisites for {target}: {format_list(prerequisites)}"
        return f"{target} is a foundational topic with no recorded prerequisites in the graph."

    # 5. RELATED TOPICS (Connected concepts in the graph)
    if any(
        word in q for word in ["related", "connected", "leads to", "next", "after", "depends on", "associated"]
    ):
        rel = get_related_topics(topic)
        lines = [f"Related concepts for {topic} (from Knowledge Graph):"]
        lines.append("• Prerequisites (incoming): " + (", ".join(rel["prerequisites"]) if rel["prerequisites"] else "None"))
        lines.append("• Next / Dependent topics (outgoing): " + (", ".join(rel["next_topics"]) if rel["next_topics"] else "None"))
        if rel["domains"]:
            lines.append(f"• Domain: {', '.join(rel['domains'])}")
        if rel["same_domain"]:
            lines.append(f"• Other topics in {', '.join(rel['domains'])}: {', '.join(rel['same_domain'])}")
        return "\n".join(lines)

    # 6. DOMAIN (Mathematics, Software, or Hardware)
    if any(
        word in q for word in ["domain", "belong", "part of", "under", "members of", "topics in", "category"]
    ):
        domain = next((e for e in entities if e in ["Mathematics", "Software", "Hardware"]), None)
        if domain:
            members = get_domain_members(domain)
            return f"Topics belonging to the {domain} domain: {format_list(members)}"
        domains = get_topic_domains(topic)
        if domains:
            return f"{topic} belongs to the {domains[0]} domain."
        return f"No domain relationship is recorded for {topic}."

    # 7. EXAMPLES (Practical examples of the concept)
    if any(
        word in q for word in ["example", "examples", "application", "applications", "use case", "real world", "practical"]
    ):
        examples = info.get("examples", "No practical examples recorded yet.")
        return f"Practical examples of {topic}: {examples}"

    # Fallback: Complete summary combining Knowledge Graph relations + Definition
    rel = get_related_topics(topic)
    definition = info.get("definition", "")
    details = [f"Topic: {topic}"]
    if definition:
        details.append(f"Definition: {definition}")
    details.append("Domain: " + (", ".join(rel["domains"]) if rel["domains"] else "Domain node"))
    details.append("Prerequisites: " + (", ".join(rel["prerequisites"]) if rel["prerequisites"] else "None recorded"))
    details.append("Leads to: " + (", ".join(rel["next_topics"]) if rel["next_topics"] else "None recorded"))
    return "\n".join(details)