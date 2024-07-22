import os
import shutil

def file_organizer(base_directory):
    
    directory_paths = [
        os.path.join(base_directory, "imgs"),
        os.path.join(base_directory, "videos"),
        os.path.join(base_directory, "documents"),
        os.path.join(base_directory, "programming"),
        os.path.join(base_directory, "compressed")
    ]
    
    file_types = {
        "imgs": [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".raw", ".svg"
        ],
        "videos": [
            ".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp"
        ], 
        "documents": [
            ".pdf", ".ppk", ".eps", ".ai", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".csv", ".xml", ".json", ".rtf", ".md", ".htm"
        ],
        "programming": [
            ".py", ".ipynb", ".pkl", ".java", ".js", ".c", ".cpp", ".h", ".cs", ".go", ".php", ".rb", ".swift", ".ts", ".html", ".css", ".sh"
        ],
        "compressed": [
            ".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".a", ".ar", ".z", ".iso", ".zst"
        ]
    }
    
    for directory in directory_paths:
        os.makedirs(directory, exist_ok=True)
        
    for file in os.listdir(base_directory):
        file_path = os.path.join(base_directory, file)
        
        if os.path.isdir(file_path):
            continue
        
        file_name, file_extension = os.path.splitext(file)
        
        for directories, extentions in file_types.items():
            if file_extension.lower() in extentions:
                target_directory = os.path.join(base_directory, directories)
                shutil.move(file_path, os.path.join(target_directory, file))
                
    print("Files Organized")

file_organizer(r"C:\Users\Admin\Downloads")