


class Base:

    def __init__(
        self,
        local_rdb_repo: BaseRDBRepository,
        remote_s3_repo: S3Repository,
    ):
        self._local_rdb_repo = local_rdb_repo
        self._remote_s3_repo = remote_s3_repo
