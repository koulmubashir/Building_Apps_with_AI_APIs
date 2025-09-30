import csv
from youtube_search import YoutubeSearch

# Perform the YouTube search
results = YoutubeSearch('Coke Studio', max_results=10).to_dict()

# Specify the CSV file name
csv_file = 'youtube_search_results.csv'

# Save the results to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Results saved to {csv_file}")

# returns a dictionary