# ProcTHOR-10K Dataset

ProcTHOR-10K is distributed with the [prior package](https://github.com/allenai/prior):

```bash
pip install prior
```

Then to use it in Python, simply run:
```python
import prior
prior.load_dataset("procthor-10k")
```

## Usage

To use the ProcTHOR-10K dataset, checkout the [Colab demo](https://colab.research.google.com/drive/1Il6TqmRXOkzYMIEaOU9e4-uTDTIb5Q78) on the [ProcTHOR website](https://procthor.allenai.org/).

## Citation

The ProcTHOR-10K dataset comes from the ProcTHOR paper:

```bibtex
@inproceedings{procthor,
  author={Matt Deitke and Eli VanderBilt and Alvaro Herrasti and
          Luca Weihs and Jordi Salvador and Kiana Ehsani and
          Winson Han and Eric Kolve and Ali Farhadi and
          Aniruddha Kembhavi and Roozbeh Mottaghi},
  title={{ProcTHOR: Large-Scale Embodied AI Using Procedural Generation}},
  booktitle={NeurIPS},
  year={2022},
  note={Outstanding Paper Award}
}
```
