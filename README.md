# README.md

## Overview

This repository contains most of the experimental data in the paper. 

## Folder Structure

### 1. **unifuzz**

The `unifuzz` directory contains essential information for the **UNIFUZZ benchmark**. We provide the generators obtained from the experiment, the seeds generated during execution, and the fuzzing logs.

#### Contents:
- **G2FUZZ_GPT35 & G2FUZZ_GPT4**: Generators specifically designed for fuzzing using GPT-3.5 and GPT-4, respectively.
- **cmplog/fast/mopt/rare**: different modes of AFL++:



### 2. **line_coverage**

The `line_coverage` folder provides the results of fuzzing and coverage measurement logs for G2FUZZ/FormatFuzzer/WEIZZ. 


### 3. **fuzztruction-experiments**

The `fuzztruction-experiments` directory contains all setting files needed to reproduce experiments conducted with Fuzztruction.
You can reproduce the experiments using the pre-built Docker image provided by Fuzztruction.