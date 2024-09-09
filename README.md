# Illumio-technical-assessment

Here is the description of my implementation.

## Assumptions:
1.I assume sufficient data: Each log entry should have at least 8 elements after splitting, or else it will be skipped.

2.The script assumes that the logs are whitespace-delimited (line.split())

3.I assume Python version is 3.x.

4.I assume all the files(lookup_table.csv, flows_log.txt, README.md) are prepared

5.The only version that is supported is 2.



## Instructions to run the code
Prerequisites:

1.Python Installations

2.Files prepared:

2.1 Lookup table

2.1.1 Column 1: Ports (comma-separated values in one cell if multiple ports are related to the same tag and protocol)

2.1.2 Column 2: Protocol

2.1.3 Column 3: Tag

Log File (flow_logs.txt): Ensure this file is formatted such that each log entry is a space-separated line where the destination port is the 6th element and the protocol number is the 8th element.

3.Running the script
Navigate to the directory and run the script(python3 solution.py)