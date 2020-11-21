import glob

def get_paths(input_folder):
    paths_ = glob.glob(input_folder+ "/*.txt")
    return paths_


def load_text(txt_path):
    with open(txt_path, "r", encoding='utf-8') as infile:
        content = infile.read()
    return content

