# codepipeline-sample

## 前提条件

すでに、codecommit にアクセスするための認証情報は登録済みで、sshによる接続設定は完了している。

## 構築

まず、codecommitを作成(ない場合)

```
$ aws cloudformation deploy --template-file ./settings/codecommit.yml --stack-name codecommit-demo
```

template.ymlとソースコードをGit Push する。


CodePipeline作成用のCFnを実行してlambdaをデプロイする。

```
aws cloudformation deploy --template-file codepipeline.yml --capabilities CAPABILITY_NAMED_IAM \
--stack-name lambda-deploy --parameter-overrides \
CodeCommitRepositoryName=test-repository PipelineName=lambda-deploy-pipeline BucketName=kentodemopipeline
```
