# VORTEX AWS環境　課金状況通知ボット

- デプロイ用コマンド（メモです
```
sam build
sam package --s3-bucket ARTIFACT --output-template-file packaged.yml
sam deploy --template-file ./packaged.yml --stack-name billingNotify --region ap-northeast-1 --capabilities CAPABILITY_IAM
```

