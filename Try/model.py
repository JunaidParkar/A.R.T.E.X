import pickle
import nltk

def tokenise(sentence: str):
    return nltk.word_tokenize(sentence)

def read_binary_file(filename):
    with open(filename, 'rb') as file:
        serialized_data = file.read()
    data = pickle.loads(serialized_data)
    return data

def wordPercentageCalculator(query_tokenised: str, responses_filtered: str):
    set1 = set(query_tokenised)
    percentile_list = []
    for response in responses_filtered:
        set2 = set(response[1])

        intersection = len(set2.intersection(set1))
        union = len(set2.union(set1))

        similarity_percentage = (intersection / union) * 100

        percentile_list.append(similarity_percentage)

    if all(num == 0 for num in percentile_list):
        return [-1]
    return percentile_list

def artex(query: str):
    datasets = read_binary_file("db1.bin")
    responses = read_binary_file("db2.bin")

    query = tokenise(query)

    filtered_responses_1 = []

    for index, dataset in enumerate(datasets):
        found_response = []
        for word in query:
            if word in dataset[1] and dataset[1] not in found_response:
                filtered_responses_1.append([index, dataset[1]])
                found_response.append(dataset[1])

    #  Writing to text file
    with open("text.txt", 'w+') as file:
        for item in filtered_responses_1:
            file.write(f"{item}\n")


    percentages = wordPercentageCalculator(query, filtered_responses_1)
    if percentages[0] == -1:
        print("Invalid query")
        return -1
    max_index, max_percentage = max(enumerate(percentages), key=lambda x: x[1])
    print(percentages)
    max_percentage = max(percentages)
    
    # Find all indices with the maximum percentage
    indices_with_max_percentage = [index for index, percentage in enumerate(percentages) if percentage == max_percentage]
    # print(percentages)
    print(f"\n {indices_with_max_percentage}")
    # print(indices_with_max_percentage)
    # Print the results
    # for index in indices_with_max_percentage:
    #     print(f"Highest Similarity: Index {index}, Percentage {max_percentage}%")

    # print(filtered_responses_1)
    tags = [filtered_responses_1[ind] for ind in indices_with_max_percentage]
    # print(tags)

artex("its time to")