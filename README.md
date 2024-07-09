# Search_engine

a dummy search engine using c++,python, javascript and more

### Fabulous Search Engine

The Fabulous Search Engine is a project developed in Python using FastAPI, websockets, and pybind11 for efficient page ranking calculations with C++ integration.

## Getting Started

### Prerequisites

Before running the search engine, ensure you have Python 3.x installed along with the necessary dependencies listed in `requirements.txt`. You can install them using pip:

```bash
pip install -r requirements.txt
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jero98772/Search_engine
   cd fabulous-search-engine
   ```

2. Install dependencies:

   ```bash
   pip install setuptools pybind11
   python setup.py install
   ```

### Running the Search Engine

To start the search engine, use the following command:

```bash
python3 -m uvicorn main:app --reload
```



This will launch the FastAPI server with auto-reload enabled.

### Data Storage

The search engine uses JSON for storing data. Ensure the necessary permissions are set for the data directory.

### Integration with C++ Page Rank Algorithm

The search engine utilizes pybind11 to connect Python with C++ for efficient page ranking calculations. Make sure C++ compiler and pybind11 are properly set up for seamless integration.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the gplv3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [FastAPI](https://fastapi.tiangolo.com/) and [pybind11](https://pybind11.readthedocs.io/) for their excellent libraries.
