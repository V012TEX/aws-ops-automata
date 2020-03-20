# VORTEX AWS環境　課金状況通知ボット

## 事前準備
### 環境変数
#### ENV_NAME
- ボットに表示する名前。VORTEX-AWSとか。
#### TOCARO_URL
- 投稿先のIncomming web hookのURL

- デプロイ用コマンドメモ
```
sam build
sam package --s3-bucket ops-automata.aws.vortex.ctcs --output-template-file packaged.yml
sam deploy --template-file ./packaged.yml --stack-name cfn-billingNotify --region ap-northeast-1 --capabilities CAPABILITY_IAM
```

