import os


class Files_manip:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.src_dir = self.config.get_config()["folders"]["src"]
        self.dest_dir = self.config.get_config()["folders"]["dest"]
        self.create_destination_folders(self.src_dir)

    def create_destination_folders(self, base_dir):
        for obj_name in os.listdir(base_dir):
            dir_path_src = os.path.join(base_dir, obj_name)
            if os.path.isdir(dir_path_src):
                dir_path_dest = self.get_destination_path(dir_path_src)
                if not os.path.exists(dir_path_dest):
                    os.mkdir(dir_path_dest)
                    self.logger.logger.info("Create new directory at {}".format(dir_path_dest))
                self.create_destination_folders(dir_path_src)

    def get_destination_path(self, src_path):
        return src_path.replace(self.src_dir, self.dest_dir)
