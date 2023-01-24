## 距離センサによる回転検出

シャープの距離センサを用いてファンの回転状態を検出する

## ラズパイのバージョン
```
lsb_release -a
No LSB modules are available.
Distributor ID: Raspbian
Description:    Raspbian GNU/Linux 10 (buster)
Release:        10
Codename:       buster
```

### OSイメージファイル
2021-05-07-raspios-buster-armhf.img  
http://ftp.jaist.ac.jp/pub/raspberrypi/raspios_arm64/images/raspios_arm64-2021-05-28/2021-05-07-raspios-buster-arm64.zip


## 使用したセンサー類
*  [１０ｂｉｔ　２ｃｈ　ＡＤコンバータ　ＭＣＰ３００２－Ｉ／Ｐ: 半導体(モジュール) 秋月電子通商-電子部品・ネット通販](https://akizukidenshi.com/catalog/g/gI-02584/)
*  [シャープ測距モジュール　ＧＰ２Ｙ０Ａ２１ＹＫ: センサ一般 秋月電子通商-電子部品・ネット通販](https://akizukidenshi.com/catalog/g/gI-02551/)

## 環境構築

```
git clone https://github.com/kmchord9/raspi_distance_sensor.git

cd raspi_distance_sensor

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

```

## イメージ書き込み後初期設定

下記でユーザー名とホスト名を変更
```
sudo raspi-config
1>S3 Password
1>S4 Hostname

1>S5>B1 コンソールのオートログインOFF
1>S5>B3 デスクトップのオートログインOFF

3>P4 spiを有効
```

piユーザー名を変更
```
sudo useradd -M tmp
sudo gpasswd -a tmp sudo
sudo passwd tmp

sudo usermod -d /home/{username} -m {username} (※{username}はユーザー名)
sudo groupmod -n {username} pi
sudo reboot
```

## ラズパイ起動時

```
sudo pigpiod
```

自動で行う場合には
```
sudo raspi-config
3>P8 Remote GPIOをYes

sudo systemctl enable pigpiod
```

## 参考文献
[Raspberry Piにシャープ製の赤外線距離センサー”GP2Y0A710K”つけてみた: EeePCの軌跡](https://arkouji.cocolog-nifty.com/blog/2015/12/raspberry-pigp2.html)
[pigpiodがsystemdサービスで自動起動しない /etc/rc.localに登録して自動起動させる - DreamerDreamのブログ](https://dreamerdream.hateblo.jp/entry/2021/07/13/170000)
[腹腹開発: pigpiod を systemctl で起動しようとしたら 8888 番ポートがすでに使われていて動作しないと怒られた件](https://fight-tsk.blogspot.com/2020/12/pigpiod-systemctl-8888.html)
