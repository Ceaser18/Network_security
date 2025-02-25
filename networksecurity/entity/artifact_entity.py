from dataclasses import dataclass
#decorator for an empty class

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
