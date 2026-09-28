import re

log = """[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage" """

pattern = r'\[(?P<timestamp>[^]]+)\]\s+(?P<level>ERROR|WARN|INFO)\s+user=(?P<user>\w+)\s+msg="(?P<msg>[^"]+)"'

entries = []

for match in re.finditer(pattern, log):
    entries.append(match.groupdict())

print("Parsed Entries:")
for entry in entries:
    print(entry)

print("\nSummary:")
print("ERROR:", len(re.findall(r'\]\s+ERROR\s+', log)))
print("WARN:", len(re.findall(r'\]\s+WARN\s+', log)))
print("INFO:", len(re.findall(r'\]\s+INFO\s+', log)))

redacted_log = re.sub(r'user=\w+', 'user=<hidden>', log)

print("\nRedacted Log:")
print(redacted_log)

entries.sort(key=lambda x: x["user"])

print("ERROR Entries:")
for entry in entries:
    if entry["level"] == "ERROR":
        print(entry["user"], ":", entry["msg"])

# Output:
# Parsed Entries:
# {'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
# {'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}
# {'timestamp': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}
#
# Summary:
# ERROR: 1
# WARN: 1
# INFO: 1
#
# Redacted Log:
# [2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
# [2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
# [2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"
#
# ERROR Entries:
# jsmith : Disk quota exceeded
