import pandas as pd
import json
import os
from typing import Union, Dict, List, Optional

class FileHandler:
    """A class to handle CSV, XLSX, and JSON file operations and combine into a single DataFrame."""

    @staticmethod
    def read_csv(file_path: str) -> pd.DataFrame:
        """Read a CSV file into a pandas DataFrame."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"CSV file not found: {file_path}")
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return pd.DataFrame()

    @staticmethod
    def read_xlsx(file_path: str) -> pd.DataFrame:
        """Read an XLSX file into a pandas DataFrame."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"XLSX file not found: {file_path}")
            return pd.read_excel(file_path)
        except Exception as e:
            print(f"Error reading XLSX: {e}")
            return pd.DataFrame()

    @staticmethod
    def read_json(file_path: str) -> pd.DataFrame:
        """Read a JSON file into a pandas DataFrame."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"JSON file not found: {file_path}")
            with open(file_path, 'r') as file:
                data = json.load(file)
            # Assume JSON is a list of dictionaries; convert to DataFrame
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Error reading JSON: {e}")
            return pd.DataFrame()

    @staticmethod
    def write_output(df: pd.DataFrame, output_path: str) -> bool:
        """Write the DataFrame to an output file based on its extension."""
        try:
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
            
            file_ext = os.path.splitext(output_path)[1].lower()
            
            if file_ext == ".csv":
                df.to_csv(output_path, index=False)
                print(f"Output written successfully to {output_path} (CSV)")
            elif file_ext == ".xlsx":
                df.to_excel(output_path, index=False)
                print(f"Output written successfully to {output_path} (XLSX)")
            elif file_ext == ".json":
                # Convert DataFrame to JSON (list of dictionaries)
                df.to_json(output_path, orient='records', indent=4)
                print(f"Output written successfully to {output_path} (JSON)")
            else:
                raise ValueError(f"Unsupported output file extension: {file_ext}")
            return True
        except Exception as e:
            print(f"Error writing output: {e}")
            return False

    @classmethod
    def combine_files(cls, file_paths: List[str], output_path: Optional[str] = None) -> pd.DataFrame:
        """Process CSV, XLSX, and JSON files and combine into a single DataFrame."""
        dataframes = []
        
        for file_path in file_paths:
            file_ext = os.path.splitext(file_path)[1].lower()
            file_name = os.path.basename(file_path)
            
            if file_ext == ".csv":
                df = cls.read_csv(file_path)
                if not df.empty:
                    print(f"Processed CSV: {file_name} with {len(df)} rows")
                    dataframes.append(df)
                else:
                    print(f"Failed to process CSV: {file_name}")
                    
            elif file_ext == ".xlsx":
                df = cls.read_xlsx(file_path)
                if not df.empty:
                    print(f"Processed XLSX: {file_name} with {len(df)} rows")
                    dataframes.append(df)
                else:
                    print(f"Failed to process XLSX: {file_name}")
                    
            elif file_ext == ".json":
                df = cls.read_json(file_path)
                if not df.empty:
                    print(f"Processed JSON: {file_name} with {len(df)} rows")
                    dataframes.append(df)
                else:
                    print(f"Failed to process JSON: {file_name}")
                    
            else:
                print(f"Unsupported file type: {file_ext} for {file_name}")

        if not dataframes:
            print("No valid dataframes to combine.")
            return pd.DataFrame()

        # Combine all DataFrames
        combined_df = pd.concat(dataframes, ignore_index=True)
        
        # Remove duplicates based on all columns
        deduplicated_df = combined_df.drop_duplicates()
        
        print(f"\nCombined DataFrame: {len(combined_df)} rows (before deduplication)")
        print(f"Final DataFrame: {len(deduplicated_df)} rows (after deduplication)")
        
        # Save to output file if output_path is provided
        if output_path and not deduplicated_df.empty:
            cls.write_output(deduplicated_df, output_path)
        
        # Display preview
        if not deduplicated_df.empty:
            print("\nFinal Combined DataFrame Preview:")
            print(deduplicated_df.head())
        else:
            print("No data to display.")
        
        return deduplicated_df

# Example usage
if __name__ == "__main__":
    handler = FileHandler()

    # List of attached file paths (replace with actual paths of your files)
    attached_files = [
        "data.csv",
        "data.xlsx",
        "data.json"
    ]

    # Combine files into a single DataFrame
    # Set output_path to None for no file output, or specify a path to save
    final_df = handler.combine_files(
        file_paths=attached_files,
        output_path="output/combined_output.csv"  # Optional: remove or change to save
    )

    # Example of using the returned DataFrame
    if not final_df.empty:
        print("\nUsing the DataFrame:")
        print(f"Number of rows: {len(final_df)}")
        print(f"Columns: {list(final_df.columns)}")











# import pandas as pd
# import json
# import os
# from typing import Union, Dict, List

# class FileHandler:
#     """A class to handle CSV, XLSX, and JSON file operations dynamically."""

#     @staticmethod
#     def read_csv(file_path: str) -> pd.DataFrame:
#         """Read a CSV file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"CSV file not found: {file_path}")
#             return pd.read_csv(file_path)
#         except Exception as e:
#             print(f"Error reading CSV: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def write_csv(data: pd.DataFrame, file_path: str) -> bool:
#         """Write a pandas DataFrame to a CSV file."""
#         try:
#             data.to_csv(file_path, index=False)
#             print(f"CSV written successfully to {file_path}")
#             return True
#         except Exception as e:
#             print(f"Error writing CSV: {e}")
#             return False

#     @staticmethod
#     def read_xlsx(file_path: str) -> pd.DataFrame:
#         """Read an XLSX file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"XLSX file not found: {file_path}")
#             return pd.read_excel(file_path)
#         except Exception as e:
#             print(f"Error reading XLSX: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def write_xlsx(data: pd.DataFrame, file_path: str) -> bool:
#         """Write a pandas DataFrame to an XLSX file."""
#         try:
#             data.to_excel(file_path, index=False)
#             print(f"XLSX written successfully to {file_path}")
#             return True
#         except Exception as e:
#             print(f"Error writing XLSX: {e}")
#             return False

#     @staticmethod
#     def read_json(file_path: str) -> Union[Dict, List]:
#         """Read a JSON file into a Python dictionary or list."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"JSON file not found: {file_path}")
#             with open(file_path, 'r') as file:
#                 return json.load(file)
#         except Exception as e:
#             print(f"Error reading JSON: {e}")
#             return {}

#     @staticmethod
#     def write_json(data: Union[Dict, List], file_path: str) -> bool:
#         """Write a Python dictionary or list to a JSON file."""
#         try:
#             with open(file_path, 'w') as file:
#                 json.dump(data, file, indent=4)
#             print(f"JSON written successfully to {file_path}")
#             return True
#         except Exception as e:
#             print(f"Error writing JSON: {e}")
#             return False

#     @classmethod
#     def process_file(cls, file_path: str, output_dir: str = "output") -> None:
#         """Process a file based on its extension and write to output directory."""
#         try:
#             # Ensure output directory exists
#             os.makedirs(output_dir, exist_ok=True)
            
#             # Get file extension and base name
#             file_ext = os.path.splitext(file_path)[1].lower()
#             file_name = os.path.basename(file_path)
#             output_path = os.path.join(output_dir, f"processed_{file_name}")

#             if file_ext == ".csv":
#                 # Read and process CSV
#                 data = cls.read_csv(file_path)
#                 if not data.empty:
#                     print(f"\nProcessing CSV: {file_name}")
#                     print("Data Preview:")
#                     print(data.head())
#                     cls.write_csv(data, output_path)
#                 else:
#                     print(f"Failed to process CSV: {file_name}")

#             elif file_ext == ".xlsx":
#                 # Read and process XLSX
#                 data = cls.read_xlsx(file_path)
#                 if not data.empty:
#                     print(f"\nProcessing XLSX: {file_name}")
#                     print("Data Preview:")
#                     print(data.head())
#                     cls.write_xlsx(data, output_path)
#                 else:
#                     print(f"Failed to process XLSX: {file_name}")

#             elif file_ext == ".json":
#                 # Read and process JSON
#                 data = cls.read_json(file_path)
#                 if data:
#                     print(f"\nProcessing JSON: {file_name}")
#                     print("Data Preview (first few items):")
#                     print(json.dumps(data[:5] if isinstance(data, list) else data, indent=2))
#                     cls.write_json(data, output_path)
#                 else:
#                     print(f"Failed to process JSON: {file_name}")

#             else:
#                 print(f"Unsupported file type: {file_ext} for {file_name}")

#         except Exception as e:
#             print(f"Error processing {file_name}: {e}")

# # Example usage
# if __name__ == "__main__":
#     handler = FileHandler()

#     # List of attached file paths (replace with actual paths of your files)
#     attached_files = [
#         "data.csv",
#         "data.xlsx",
#         "data.json"
#     ]

#     # Process each file
#     for file_path in attached_files:
#         handler.process_file(file_path, output_dir="processed_output")
# Generates duplicate doutput files





# import pandas as pd
# import json
# import os
# from typing import Union, Dict, List

# class FileHandler:
#     """A class to handle CSV, XLSX, and JSON file operations and combine into a single DataFrame."""

#     @staticmethod
#     def read_csv(file_path: str) -> pd.DataFrame:
#         """Read a CSV file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"CSV file not found: {file_path}")
#             return pd.read_csv(file_path)
#         except Exception as e:
#             print(f"Error reading CSV: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def read_xlsx(file_path: str) -> pd.DataFrame:
#         """Read an XLSX file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"XLSX file not found: {file_path}")
#             return pd.read_excel(file_path)
#         except Exception as e:
#             print(f"Error reading XLSX: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def read_json(file_path: str) -> pd.DataFrame:
#         """Read a JSON file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"JSON file not found: {file_path}")
#             with open(file_path, 'r') as file:
#                 data = json.load(file)
#             # Assume JSON is a list of dictionaries; convert to DataFrame
#             return pd.DataFrame(data)
#         except Exception as e:
#             print(f"Error reading JSON: {e}")
#             return pd.DataFrame()

#     @classmethod
#     def combine_files(cls, file_paths: List[str]) -> pd.DataFrame:
#         """Process CSV, XLSX, and JSON files and combine into a single DataFrame."""
#         dataframes = []
        
#         for file_path in file_paths:
#             file_ext = os.path.splitext(file_path)[1].lower()
#             file_name = os.path.basename(file_path)
            
#             if file_ext == ".csv":
#                 df = cls.read_csv(file_path)
#                 if not df.empty:
#                     print(f"Processed CSV: {file_name} with {len(df)} rows")
#                     dataframes.append(df)
#                 else:
#                     print(f"Failed to process CSV: {file_name}")
                    
#             elif file_ext == ".xlsx":
#                 df = cls.read_xlsx(file_path)
#                 if not df.empty:
#                     print(f"Processed XLSX: {file_name} with {len(df)} rows")
#                     dataframes.append(df)
#                 else:
#                     print(f"Failed to process XLSX: {file_name}")
                    
#             elif file_ext == ".json":
#                 df = cls.read_json(file_path)
#                 if not df.empty:
#                     print(f"Processed JSON: {file_name} with {len(df)} rows")
#                     dataframes.append(df)
#                 else:
#                     print(f"Failed to process JSON: {file_name}")
                    
#             else:
#                 print(f"Unsupported file type: {file_ext} for {file_name}")

#         if not dataframes:
#             print("No valid dataframes to combine.")
#             return pd.DataFrame()

#         # Combine all DataFrames
#         combined_df = pd.concat(dataframes, ignore_index=True)
        
#         # Remove duplicates based on all columns
#         deduplicated_df = combined_df.drop_duplicates()
        
#         print(f"\nCombined DataFrame: {len(combined_df)} rows (before deduplication)")
#         print(f"Final DataFrame: {len(deduplicated_df)} rows (after deduplication)")
        
#         return deduplicated_df

# # Example usage
# if __name__ == "__main__":
#     handler = FileHandler()

#     # List of attached file paths (replace with actual paths of your files)
#     attached_files = [
#         "data.csv",
#         "data.xlsx",
#         "data.json"
#     ]

#     # Combine files into a single DataFrame
#     final_df = handler.combine_files(attached_files)
    
#     # Display the final DataFrame
#     if not final_df.empty:
#         print("\nFinal Combined DataFrame Preview:")
#         print(final_df.head())
#     else:
#         print("No data to display.")
# reads all three files






# import pandas as pd
# import json
# import os
# from typing import Union, Dict, List

# class FileHandler:
#     """A class to handle CSV, XLSX, and JSON file operations, combine into a single DataFrame, and save to an output file."""

#     @staticmethod
#     def read_csv(file_path: str) -> pd.DataFrame:
#         """Read a CSV file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"CSV file not found: {file_path}")
#             return pd.read_csv(file_path)
#         except Exception as e:
#             print(f"Error reading CSV: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def read_xlsx(file_path: str) -> pd.DataFrame:
#         """Read an XLSX file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"XLSX file not found: {file_path}")
#             return pd.read_excel(file_path)
#         except Exception as e:
#             print(f"Error reading XLSX: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def read_json(file_path: str) -> pd.DataFrame:
#         """Read a JSON file into a pandas DataFrame."""
#         try:
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"JSON file not found: {file_path}")
#             with open(file_path, 'r') as file:
#                 data = json.load(file)
#             # Assume JSON is a list of dictionaries; convert to DataFrame
#             return pd.DataFrame(data)
#         except Exception as e:
#             print(f"Error reading JSON: {e}")
#             return pd.DataFrame()

#     @staticmethod
#     def write_output(df: pd.DataFrame, output_path: str) -> bool:
#         """Write the DataFrame to an output file based on its extension."""
#         try:
#             # Ensure output directory exists
#             os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
            
#             file_ext = os.path.splitext(output_path)[1].lower()
            
#             if file_ext == ".csv":
#                 df.to_csv(output_path, index=False)
#                 print(f"Output written successfully to {output_path} (CSV)")
#             elif file_ext == ".xlsx":
#                 df.to_excel(output_path, index=False)
#                 print(f"Output written successfully to {output_path} (XLSX)")
#             elif file_ext == ".json":
#                 # Convert DataFrame to JSON (list of dictionaries)
#                 df.to_json(output_path, orient='records', indent=4)
#                 print(f"Output written successfully to {output_path} (JSON)")
#             else:
#                 raise ValueError(f"Unsupported output file extension: {file_ext}")
#             return True
#         except Exception as e:
#             print(f"Error writing output: {e}")
#             return False

#     @classmethod
#     def combine_and_save_files(cls, file_paths: List[str], output_path: str = "output/combined_output.csv") -> pd.DataFrame:
#         """Process CSV, XLSX, and JSON files, combine into a single DataFrame, and save to an output file."""
#         dataframes = []
        
#         for file_path in file_paths:
#             file_ext = os.path.splitext(file_path)[1].lower()
#             file_name = os.path.basename(file_path)
            
#             if file_ext == ".csv":
#                 df = cls.read_csv(file_path)
#                 if not df.empty:
#                     print(f"Processed CSV: {file_name} with {len(df)} rows")
#                     dataframes.append(df)
#                 else:
#                     print(f"Failed to process CSV: {file_name}")
                    
#             elif file_ext == ".xlsx":
#                 df = cls.read_xlsx(file_path)
#                 if not df.empty:
#                     print(f"Processed XLSX: {file_name} with {len(df)} rows")
#                     dataframes.append(df)
#                 else:
#                     print(f"Failed to process XLSX: {file_name}")
                    
#             elif file_ext == ".json":
#                 df = cls.read_json(file_path)
#                 if not df.empty:
#                     print(f"Processed JSON: {file_name} with {len(df)} rows")
#                     dataframes.append(df)
#                 else:
#                     print(f"Failed to process JSON: {file_name}")
                    
#             else:
#                 print(f"Unsupported file type: {file_ext} for {file_name}")

#         if not dataframes:
#             print("No valid dataframes to combine.")
#             return pd.DataFrame()

#         # Combine all DataFrames
#         combined_df = pd.concat(dataframes, ignore_index=True)
        
#         # Remove duplicates based on all columns
#         deduplicated_df = combined_df.drop_duplicates()
        
#         print(f"\nCombined DataFrame: {len(combined_df)} rows (before deduplication)")
#         print(f"Final DataFrame: {len(deduplicated_df)} rows (after deduplication)")
        
#         # Save the final DataFrame to the output file
#         if not deduplicated_df.empty:
#             cls.write_output(deduplicated_df, output_path)
#             print("\nFinal Combined DataFrame Preview:")
#             print(deduplicated_df.head())
#         else:
#             print("No data to save.")
        
#         return deduplicated_df

# # Example usage
# if __name__ == "__main__":
#     handler = FileHandler()

#     # List of attached file paths (replace with actual paths of your files)
#     attached_files = [
#         "data.csv",
#         "data.xlsx",
#         "data.json"
#     ]

#     # Combine files and save to output file (default: CSV)
#     final_df = handler.combine_and_save_files(
#         file_paths=attached_files,
#         output_path="output/combined_output.json"
#     )
# Real and combine all files in an output file


