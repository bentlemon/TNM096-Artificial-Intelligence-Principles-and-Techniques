class Clause:
    def __init__(self, positives, negatives):
        # Initialize with lists and convert to sets to remove duplicates.
        self.positives = set(positives)
        self.negatives = set(negatives)

    def __str__(self):
        # Returns a readable format of the clause for debugging.
        positives = ' ∨ '.join(self.positives)
        negatives = ' ∨ '.join('¬' + n for n in self.negatives)
        if positives and negatives:
            return f"{positives} ∨ {negatives}"
        return positives or negatives

def resolution(clause1, clause2):
    # Simplified resolution that focuses on finding a single resolvable pair of literals.
    for p in clause1.positives:
        if p in clause2.negatives:
            new_positives = clause1.positives.union(clause2.positives) - {p}
            new_negatives = clause1.negatives.union(clause2.negatives) - {p}
            if new_positives.intersection(new_negatives):
                return None  # Result is a tautology
            return Clause(new_positives, new_negatives)

    for n in clause1.negatives:
        if n in clause2.positives:
            new_positives = clause1.positives.union(clause2.positives) - {n}
            new_negatives = clause1.negatives.union(clause2.negatives) - {n}
            if new_positives.intersection(new_negatives):
                return None  # Result is a tautology
            return Clause(new_positives, new_negatives)

    return None  # No resolution possible

def solver(kb):
    # This is a naive solver that does not handle subsumption or other optimizations.
    new_clauses = True
    while new_clauses:
        new_clauses = False
        new_kb = kb.copy()
        for clause1 in kb:
            for clause2 in kb:
                if clause1 != clause2:
                    resolved = resolution(clause1, clause2)
                    if resolved and resolved not in kb:
                        new_kb.add(resolved)
                        new_clauses = True
        kb = new_kb
    return kb

# Example of usage
kb = set([
    Clause(['a', 'b'], ['c']),
    Clause(['c'], ['b'])
])

resolved_kb = solver(kb)
for clause in resolved_kb:
    print(clause)


