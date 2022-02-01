## Planning (PM 3:11 2022-02-01)

I'm planning a separate image library. And it will be maintained using a git repo.

---

# Development Processing

Prepare the base function for the experiment.

## Dataset Prepare (AM 4:38 2022-01-16)

DIV2K *dataset* [https://data.vision.ee.ethz.ch/cvl/DIV2K/]

| Name                | Description                                   | Note |
| ------------------- | --------------------------------------------- | ---- |
| batch_processing.py | Main process for batch processing of datasets |      |
| batch_tasks.py      | Algorithm to apply batch processing           |      |

Batch processing was created based on the command pattern. You can write the necessary command in batch_tasks.py and use it to proceed with batch processing.

the follow tasks have been added.

| Name                 | Description                                | Note |
| -------------------- | :----------------------------------------- | ---- |
| Rescale              | Crop the image with the center crop method |      |
| ImageResolutionPrint | Resolution print function                  |      |
| ImageSaver           | Save image to specified output path        |      |

Convert DIV2K to 1080p wide HD using the above function.

Prepare the base function for the experiment.

## opencv development environment establishment (pm 11:11 2022-01-17)

1. Image Complexity Measure: a Human Criterion Free Approach [paper]



## Image complexity measure (pm 11:11 2022-01-17)

1. Image Complexity Measure: a Human Criterion Free Approach [paper]

