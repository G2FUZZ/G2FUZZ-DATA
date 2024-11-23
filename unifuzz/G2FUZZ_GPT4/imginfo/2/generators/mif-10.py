def create_mif_file(filename):
    content = """
Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 104
Columns 1
  ID Integer
Data

Region 1
  5
    -100.0, 100.0
    100.0, 100.0
    100.0, -100.0
    -100.0, -100.0
    -100.0, 100.0


MultiRegion 2

  Region 1
    5
      -50.0, 50.0
      -30.0, 50.0
      -30.0, 30.0
      -50.0, 30.0
      -50.0, 50.0

  Region 1
    5
      30.0, -30.0
      50.0, -30.0
      50.0, -50.0
      30.0, -50.0
      30.0, -30.0
"""
    with open(f"./tmp/{filename}.mif", "w") as file:
        file.write(content.strip())

if __name__ == "__main__":
    import os
    os.makedirs("./tmp/", exist_ok=True)
    create_mif_file("example_region_and_multiregion")