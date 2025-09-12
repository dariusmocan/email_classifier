import zipfile as zp


class DataLoader:
    def load_emails(self, zip_path):
        """Load emails from ZIP archive and return files data"""
        # Store all file contents in lists for access throughout the code
        easy_ham_data = []
        hard_ham_data = []
        spam_data = []

        with zp.ZipFile(zip_path) as z:
            # Read easy_ham emails
            easy_ham_files = [f for f in z.namelist() if f.startswith("easy_ham/easy_ham/") and not f.endswith("/")]
            for filename in easy_ham_files:
                with z.open(filename) as file:
                    try:
                        content = file.read().decode("utf-8", errors="ignore")
                        easy_ham_data.append(content)
                    except Exception as e:
                        print(f"Error reading {filename}: {e}")
            
            # Read hard_ham emails
            hard_ham_files = [f for f in z.namelist() if f.startswith("hard_ham/hard_ham/") and not f.endswith("/")]
            for filename in hard_ham_files:
                with z.open(filename) as file:
                    try:
                        content = file.read().decode("utf-8", errors="ignore")
                        hard_ham_data.append(content)
                    except Exception as e:
                        print(f"Error reading {filename}: {e}")
            
            # Read spam emails
            spam_files = [f for f in z.namelist() if f.startswith("spam_2/spam_2/") and not f.endswith("/")]
            for filename in spam_files:
                with z.open(filename) as file:
                    try:
                        content = file.read().decode("utf-8", errors="ignore")
                        spam_data.append(content)
                    except Exception as e:
                        print(f"Error reading {filename}: {e}")

        print(f"Loaded {len(easy_ham_data)} easy_ham emails")
        print(f"Loaded {len(hard_ham_data)} hard_ham emails") 
        print(f"Loaded {len(spam_data)} spam emails")
        
        return easy_ham_data, hard_ham_data, spam_data
