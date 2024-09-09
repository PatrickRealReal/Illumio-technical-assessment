import csv
from collections import defaultdict

def read_lookup_table(filename):
    tag_dict = defaultdict(list)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            ports = row[0].split(',')
            protocol = row[1]
            tag = row[2]
            for port in ports:
                tag_dict[(port.strip(), protocol.strip())].append(tag.strip())
    return tag_dict

def process_logs(log_filename, lookup_dict):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    with open(log_filename, 'r') as file:
        for line in file:
            parts = line.split()
            version_number = parts[0]
            if version_number != '2':
                continue  
            dst_port = parts[5]
            protocol_num = parts[7]
            protocol = 'tcp' if protocol_num == '6' else 'udp' if protocol_num == '17' else 'icmp' if protocol_num == '1' else 'unknown'

            key = (dst_port, protocol)
            port_protocol_counts[key] += 1

            if key in lookup_dict:
                for tag in lookup_dict[key]:
                    tag_counts[tag] += 1
            else:
                tag_counts['Untagged'] += 1

    return tag_counts, port_protocol_counts

# Main function to tie everything together
def main(lookup_filename, log_filename):
    lookup_dict = read_lookup_table(lookup_filename)
    tag_counts, port_protocol_counts = process_logs(log_filename, lookup_dict)

    # Output tag counts
    print("Tag Counts:")
    print("Tag,Count")
    for tag, count in tag_counts.items():
        print(f"{tag},{count}")

    # Output port/protocol combination counts
    print("\nPort/Protocol Combination Counts:")
    print("Port,Protocol,Count")
    for (port, protocol), count in port_protocol_counts.items():
        print(f"{port},{protocol},{count}")

main('lookup_table.csv', 'flow_logs.txt')