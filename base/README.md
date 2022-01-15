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



