# Commands for uploading

Update version in `setup.py` and execute the following commands.

```
sudo pip3 install twine
sudo rm -r dist
sudo python3 setup.py sdist bdist_wheel
twine upload dist/*
```

# References
- [Pythonで作成したライブラリを、PyPIに公開/アップロードする](https://qiita.com/icoxfog417/items/edba14600323df6bf5e0)
- [Packaging and Distributing Projects](https://packaging.python.org/tutorials/distributing-packages/)
