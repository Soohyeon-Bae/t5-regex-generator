# T5-based Regular Expression Generation Model

This mini project uses the T5 model to **convert tagged strings into regular expressions using NLP techniques**.

## Features

- `train.py` → Trains and saves the T5 model
- `generate.py` → Generates regular expressions from tagged input using the trained model
 
## Project Structure

The repository is organized as follows:

t5-regex-generator/  
│── 📂 data/                                                                                                                                                                                      
│   ├── regex_data.csv          
│── 📂 models/                  
│   ├── t5_regex_model/         
│── 📂 src/                    
│   ├── train.py                
│   ├── generate.py            
│   ├── dataset.py              
│── 📂 notebooks/               
│   ├── t5_regex_training.ipynb                                                                        
│── .gitignore                  
│── requirements.txt            
└── README.md                   

## Installation
To set up the project, clone the repository and install the required packages:

````
pip install -r requirements.txt
````

## Usage

Ensure the `data/regex_data.csv` file contains correctly formatted training data.

### Train the Model

````
python src/train.py
````

### Test Regular Expression Generation

````
python src/generate.py
````

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project follows the MIT License.





