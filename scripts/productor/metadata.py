from pathlib import Path
import config
import os
import time

class Metadata:
    def __init__(self,data_dir_path = config.DATA_PATH):
        self.data_dir_path = data_dir_path

    def get_file_metadata(self, file):
        name = file.name
        stats = os.stat(file)
        size_kbs = stats.st_size * 0.000125
        size_bites = stats.st_size
        creation_datetime = time.ctime(stats.st_ctime)
        creation_time = stats.st_ctime
        last_change_datetime = time.ctime(stats.st_mtime)
        last_accessed_datetime = time.ctime(stats.st_atime)

        metadata = {
            'filepath': str(file),
            'filename': name,
            'size_kbs': size_kbs,
            'size_bites': size_bites,
            'creation_datetime': creation_datetime,
            'creation_time': creation_time,
            'last_change_datetime': last_change_datetime,
            'last_accessed_datetime': last_accessed_datetime
        }
        return metadata

    def get_all_files_metadata(self):
        metadata_list = list()
        for file in Path(self.data_dir_path).glob("*.wav"):
            if file.is_file():
                metadata = self.get_file_metadata(file)
                metadata_list.append(metadata)
        return metadata_list
