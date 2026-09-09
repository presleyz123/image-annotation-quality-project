import csv
from collections import Counter

FILE_PATH = "data/sample_annotations.csv"


def load_annotations(file_path):
    """Load annotation records from a CSV file."""
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def analyze_annotations(records):
    """Calculate basic statistics about the annotations."""
    total = len(records)

    labels = Counter(record["object_label"] for record in records)

    confidence_scores = [
        float(record["confidence"])
        for record in records
    ]

    average_confidence = sum(confidence_scores) / total

    return total, labels, average_confidence


def main():
    records = load_annotations(FILE_PATH)

    total, labels, average_confidence = analyze_annotations(records)

    print("IMAGE ANNOTATION DATASET ANALYSIS")
    print("---------------------------------")
    print(f"Total annotations: {total}")
    print(f"Average confidence: {average_confidence:.2f}")

    print("\nObject distribution:")
    for label, count in labels.items():
        print(f"- {label}: {count}")


if _name_ == "_main_":
    main()
