For `qpdf-enc_pdftotext-dec`, it re-uses the seeds generated in `pdfseperate_pdftotext` as they have the same input format.
For `zip_unzip`, it re-uses the seeds generated in `7zip_7zip` as they have the same input format.

We remove the seed whose size is larger than 10MB.