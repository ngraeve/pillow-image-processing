from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_sns as sns,
    aws_sqs as sqs,
    aws_iam as iam,
)
from constructs import Construct
from aws_solutions_constructs.aws_s3_lambda import S3ToLambda

class PillowImageProcessingStack(Stack):
    """
    AWS CDK stack for the Pillow image processing pipeline.
    """
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        S3ToLambda(self, 'processImage',
           lambda_function_props=_lambda.FunctionProps(
               code=_lambda.Code.from_asset('src/process_image'),
               runtime=_lambda.Runtime.PYTHON_3_12,
               handler='handler'
           )
           )