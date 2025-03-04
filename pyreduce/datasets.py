import os
import tarfile
import wget


def UVES_HD132205(local_dir=None):
    """Load an example dataset for the UVES instrument

    Parameters
    ----------
    local_dir : str, optional
        directory to save data at (default: "./")

    Returns
    -------
    dataset_dir : str
        directory where the data was saved
    """

    if local_dir is None:
        local_dir = os.path.dirname(__file__)
        local_dir = os.path.join(local_dir, "../")

    # load data if necessary
    target_dir = os.path.join(local_dir, "datasets")
    filename = os.path.join(local_dir, "uves_data.tar.gz")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if not os.path.isfile(filename):
        url = "http://www.astro.uu.se/~piskunov/RESEARCH/REDUCE/FTP/reduce_demo.tar.gz"
        wget.download(url, out=filename)

    with tarfile.open(filename) as file:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(file, path=target_dir)

    return target_dir


if __name__ == "__main__":
    UVES_HD132205()
