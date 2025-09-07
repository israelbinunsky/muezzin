from pathlib import Path
import config
import os
import time

class Metadata:
    def __init__(self):
        self.data_dir_path = f'{config.PATH}/podcasts'

    def get_file_metadata(self, file, index):
        name = file.name

        stats = os.stat(file)

        size_kbs = int(stats.st_size) * 0.000125
        creation_datetime = time.ctime(stats.st_ctime)
        last_change_datetime = time.ctime(stats.st_mtime)
        last_accessed_datetime = time.ctime(stats.st_atime)

        metadata = {
            'index': index,
            'path': str(file),
            'name': name,
            'size_kbs': size_kbs,
            'creation_datetime': creation_datetime,
            'last_change_datetime': last_change_datetime,
            'last_accessed_datetime': last_accessed_datetime
        }
        return metadata

    def get_all_files_metadata(self):
        index = 1
        metadata_list = list()
        for file in Path(self.data_dir_path).glob("*.wav"):
            if file.is_file():
                metadata = self.get_file_metadata(file, index)
                index += 1
                metadata_list.append(metadata)
        return metadata_list
