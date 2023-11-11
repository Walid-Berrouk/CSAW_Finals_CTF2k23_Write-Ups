# Hypokrinesthai

## Description

> iahtsenirkopyH

## Write-Up

```
$ ./reverse_hexdump.sh hypokrinesthai.txt > data
```

From there, we reverse the binary in the `data` file as hinted in the description

```
$ perl -0777pe '$_=reverse $_' data > reversed_data
```

After that, using the result binary, we pass it to a `from binary` function (in cyberchef for example), we get the `reverses`, which is a protugeuse text.

After looking for the `csaw` in that text, we get:

```
└─$ grep 'csaw' revevses.bin 
No commovida obrigacao le csawctf{hypocrita tu os}. Curtos ler casado mereca esposo nem avisar hombro cha. Es inspirar no pontapes condicao tu duzentos indaguei trazendo es. Affeicoas disparate abobadada diz dar vae condicoes indagaste dementava ver. Has resignados mal meditativa com meu considerou. Matar ja dante ma de se filha fazes lavar. Tragico resisto ficamos nem afogado esqueca ameigou hao pau. Pranto salvas estado mo os vencel ma soffre alguma. Hao buscando teu souberam amoravel sim irritado.
```


## Flag

csawctf{hypocrita tu os}