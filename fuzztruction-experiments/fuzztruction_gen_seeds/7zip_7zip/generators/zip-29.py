import zipfile
from datetime import datetime
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the zip file
zip_path = './tmp/advanced_metadata_storage_with_plugins.zip'

# Create a zip file with metadata and additional features
with zipfile.ZipFile(zip_path, 'w') as zipf:
    # Sample content to add to the ZIP
    sample_content = "This is some sample content for our file."
    file_name = 'sample.txt'
    
    # Additional feature content
    feature_content = """
    12. **Integration with Operating Systems**: ZIP file support is often integrated into operating system file explorers, 
    allowing users to view and manipulate ZIP files similarly to regular folders, enhancing user experience and accessibility.
    """
    feature_file_name = 'features.txt'
    
    # New feature content: Compression Method Plug-ins
    plugin_feature_content = """
    5. **Compression Method Plug-ins**: Some ZIP applications allow the use of plug-ins to extend compression capabilities with new algorithms, providing flexibility and optimization for specific types of data.
    """
    plugin_feature_file_name = 'compression_plugins.txt'
    
    # Writing the file with content
    zipf.writestr(file_name, sample_content)
    
    # Writing the additional feature file
    zipf.writestr(feature_file_name, feature_content)
    
    # Writing the plugin feature file
    zipf.writestr(plugin_feature_file_name, plugin_feature_content)
    
    # Setting metadata for the first file within the ZIP
    info = zipfile.ZipInfo(file_name)
    
    # Setting the date and time of the first file to Jan 1st, 2020, 12:00 PM
    info.date_time = (2020, 1, 1, 12, 0, 0)
    
    # Setting the file permissions to read, write, and execute for the owner, read for the group, and read for others
    info.external_attr = 0o755 << 16  # Unix attributes
    
    # Setting metadata for the additional feature file within the ZIP
    info_feature = zipfile.ZipInfo(feature_file_name)
    
    # Setting the date and time of the additional feature file to Jan 1st, 2020, 12:00 PM
    info_feature.date_time = (2020, 1, 1, 12, 0, 0)
    
    # Setting the file permissions for the additional feature file
    info_feature.external_attr = 0o644 << 16  # Unix attributes for read and write by owner, read by group and others
    
    # Setting metadata for the plugin feature file
    info_plugin_feature = zipfile.ZipInfo(plugin_feature_file_name)
    
    # Setting the date and time of the plugin feature file to Jan 1st, 2020, 12:00 PM
    info_plugin_feature.date_time = (2020, 1, 1, 12, 0, 0)
    
    # Setting the file permissions for the plugin feature file
    info_plugin_feature.external_attr = 0o644 << 16  # same as above
    
    # Adding a comment to the ZIP file
    zipf.comment = b"This is a ZIP file containing metadata and additional features including Compression Method Plug-ins."
    
    # Write the file with the specified info and metadata
    zipf.writestr(info, sample_content)
    
    # Write the additional feature file with specified info and metadata
    zipf.writestr(info_feature, feature_content)
    
    # Write the plugin feature file with specified info and metadata
    zipf.writestr(info_plugin_feature, plugin_feature_content)

print("ZIP file with metadata and additional features including Compression Method Plug-ins has been created.")