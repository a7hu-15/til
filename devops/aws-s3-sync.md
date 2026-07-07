# Syncing Folders with AWS S3

The `aws s3 sync` command only uploads files that are new or have changed.

```bash
aws s3 sync ./local-folder s3://my-bucket/path/
```
Add `--delete` to remove files in the bucket that were deleted locally.