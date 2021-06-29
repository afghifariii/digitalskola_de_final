import csv, sys

with open('flights.csv', mode='r') as csv_file:
    with open('flights_new.csv', mode='w') as flights:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(row)
            if line_count > 5000:
                sys.exit(1)
            else:
                flights_writer = csv.writer(flights, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                flights_writer.writerow(row)
                line_count += 1

        