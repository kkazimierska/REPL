# sample.py

def read_data():
    # Read data from a file or database...
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sample = read_data()

def mean(data):
    try:
        av = sum(data) / len(data)
        return av
    except ZeroDivisionError:
        print(f"You should provide the data to count the mean. \
            Provided {data}.")


average = mean(sample)
# print(average)