#!/bin/bash

echo Creating files file1, file2, file3 and file4...

touch file{1..4}
tar -czvf file_archive.tar.gz file{1..4}

echo Done