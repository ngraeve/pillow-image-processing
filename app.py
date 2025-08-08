#!/usr/bin/env python3
"""
Entry point for AWS CDK application.
"""
import aws_cdk as cdk
from infra.stack import PillowImageProcessingStack

app = cdk.App()
PillowImageProcessingStack(app, "PillowImageProcessingStack")
app.synth()
