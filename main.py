import log_reader

#regexp
regex_time = r"^\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}"
regex_req = r"(?<=INFO -).+(?=\()"
regex_data = r"(?<=\().+(?=\))"

path_log = 'C:/work/logs/log26.09.2023.log'
path_for_save = 'C:/work/logs/'

log_reader.parse_data(
    regex_time,
    regex_req,
    regex_data,
    path_log,
    path_for_save
)