from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from homePage import models as m
from . import templater
import glob

def process_request(request):

  new_sign = m.Sign()
  new_sign.id = 1
  new_sign.filepath = "/static/homePage/images/signs/001.png"
  new_sign.name = "1"
  new_sign.mimeType = "1"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 2
  new_sign.filepath = "/static/homePage/images/signs/002a.png"
  new_sign.name = "2"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 3
  new_sign.filepath = "/static/homePage/images/signs/002b.png"
  new_sign.name = "2a"
  new_sign.mimeType = "2a"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 4
  new_sign.filepath = "/static/homePage/images/signs/002c.png"
  new_sign.name = "2c"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 5
  new_sign.filepath = "/static/homePage/images/signs/002cc.png"
  new_sign.name = "2cc"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 6
  new_sign.filepath = "/static/homePage/images/signs/005.png"
  new_sign.name = "5"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 7
  new_sign.filepath = "/static/homePage/images/signs/006.png"
  new_sign.name = "6"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 8
  new_sign.filepath = "/static/homePage/images/signs/007.png"
  new_sign.name = "2"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 10
  new_sign.filepath = "/static/homePage/images/signs/010.png"
  new_sign.name = "10"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 13
  new_sign.filepath = "/static/homePage/images/signs/013.png"
  new_sign.name = "13"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 15
  new_sign.filepath = "/static/homePage/images/signs/015.png"
  new_sign.name = "15"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 26
  new_sign.filepath = "/static/homePage/images/signs/026.png"
  new_sign.name = "26"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 29
  new_sign.filepath = "/static/homePage/images/signs/029.png"
  new_sign.name = "2"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 50
  new_sign.filepath = "/static/homePage/images/signs/050.png"
  new_sign.name = "2"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 52
  new_sign.filepath = "/static/homePage/images/signs/052.png"
  new_sign.name = "2"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 53
  new_sign.filepath = "/static/homePage/images/signs/053a.png"
  new_sign.name = "53a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 54
  new_sign.filepath = "/static/homePage/images/signs/053b.png"
  new_sign.name = "53b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 55
  new_sign.filepath = "/static/homePage/images/signs/055.png"
  new_sign.name = "55"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 57
  new_sign.filepath = "/static/homePage/images/signs/057.png"
  new_sign.name = "57"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 58
  new_sign.filepath = "/static/homePage/images/signs/058.png"
  new_sign.name = "58"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 59
  new_sign.filepath = "/static/homePage/images/signs/059.png"
  new_sign.name = "59"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 61
  new_sign.filepath = "/static/homePage/images/signs/061.png"
  new_sign.name = "61"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 62
  new_sign.filepath = "/static/homePage/images/signs/062.png"
  new_sign.name = "62"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 68
  new_sign.filepath = "/static/homePage/images/signs/068.png"
  new_sign.name = "68"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 69
  new_sign.filepath = "/static/homePage/images/signs/069.png"
  new_sign.name = "69"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 70
  new_sign.filepath = "/static/homePage/images/signs/070.png"
  new_sign.name = "70"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 71
  new_sign.filepath = "/static/homePage/images/signs/071.png"
  new_sign.name = "71"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 73
  new_sign.filepath = "/static/homePage/images/signs/073.png"
  new_sign.name = ""
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 74
  new_sign.filepath = "/static/homePage/images/signs/074a.png"
  new_sign.name = "74a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 75
  new_sign.filepath = "/static/homePage/images/signs/074b.png"
  new_sign.name = "74b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 76
  new_sign.filepath = "/static/homePage/images/signs/075.png"
  new_sign.name = "75"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 78
  new_sign.filepath = "/static/homePage/images/signs/078.png"
  new_sign.name = "78"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 79
  new_sign.filepath = "/static/homePage/images/signs/079.png"
  new_sign.name = "79"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 80
  new_sign.filepath = "/static/homePage/images/signs/080.png"
  new_sign.name = "80"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 84
  new_sign.filepath = "/static/homePage/images/signs/084.png"
  new_sign.name = "84"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 85
  new_sign.filepath = "/static/homePage/images/signs/085.png"
  new_sign.name = "85"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 86
  new_sign.filepath = "/static/homePage/images/signs/086.png"
  new_sign.name = "86"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 94
  new_sign.filepath = "/static/homePage/images/signs/094.png"
  new_sign.name = "94"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 97
  new_sign.filepath = "/static/homePage/images/signs/097.png"
  new_sign.name = "97"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 99
  new_sign.filepath = "/static/homePage/images/signs/099.png"
  new_sign.name = "99"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 101
  new_sign.filepath = "/static/homePage/images/signs/101.png"
  new_sign.name = "101"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 104
  new_sign.filepath = "/static/homePage/images/signs/104.png"
  new_sign.name = "104"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 105
  new_sign.filepath = "/static/homePage/images/signs/105.png"
  new_sign.name = "105"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 106
  new_sign.filepath = "/static/homePage/images/signs/106.png"
  new_sign.name = "106"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 109
  new_sign.filepath = "/static/homePage/images/signs/109.png"
  new_sign.name = "109"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 111
  new_sign.filepath = "/static/homePage/images/signs/111.png"
  new_sign.name = "111"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 112
  new_sign.filepath = "/static/homePage/images/signs/112.png"
  new_sign.name = "112"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 114
  new_sign.filepath = "/static/homePage/images/signs/114.png"
  new_sign.name = "114"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 115
  new_sign.filepath = "/static/homePage/images/signs/115.png"
  new_sign.name = "115"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 123
  new_sign.filepath = "/static/homePage/images/signs/123.png"
  new_sign.name = "123"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 124
  new_sign.filepath = "/static/homePage/images/signs/124a.png"
  new_sign.name = "124a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 125
  new_sign.filepath = "/static/homePage/images/signs/124b.png"
  new_sign.name = "124b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 126
  new_sign.filepath = "/static/homePage/images/signs/125b.png"
  new_sign.name = "125b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 127
  new_sign.filepath = "/static/homePage/images/signs/125c.png"
  new_sign.name = "125c"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 128
  new_sign.filepath = "/static/homePage/images/signs/125d.png"
  new_sign.name = "125d"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 129
  new_sign.filepath = "/static/homePage/images/signs/125e.png"
  new_sign.name = "125e"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 130
  new_sign.filepath = "/static/homePage/images/signs/125f.png"
  new_sign.name = "125f"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 131
  new_sign.filepath = "/static/homePage/images/signs/126.png"
  new_sign.name = "126"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 132
  new_sign.filepath = "/static/homePage/images/signs/128.png"
  new_sign.name = "128"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 133
  new_sign.filepath = "/static/homePage/images/signs/130.png"
  new_sign.name = "130"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 134
  new_sign.filepath = "/static/homePage/images/signs/131.png"
  new_sign.name = "131"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 135
  new_sign.filepath = "/static/homePage/images/signs/132.png"
  new_sign.name = "132"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 136
  new_sign.filepath = "/static/homePage/images/signs/133.png"
  new_sign.name = "133"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 137
  new_sign.filepath = "/static/homePage/images/signs/134.png"
  new_sign.name = "134"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 138
  new_sign.filepath = "/static/homePage/images/signs/138.png"
  new_sign.name = "138"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 139
  new_sign.filepath = "/static/homePage/images/signs/139.png"
  new_sign.name = "139"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 142
  new_sign.filepath = "/static/homePage/images/signs/142.png"
  new_sign.name = "142"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 144
  new_sign.filepath = "/static/homePage/images/signs/144.png"
  new_sign.name = "144"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 145
  new_sign.filepath = "/static/homePage/images/signs/145.png"
  new_sign.name = "145"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 147
  new_sign.filepath = "/static/homePage/images/signs/147.png"
  new_sign.name = "147"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 148
  new_sign.filepath = "/static/homePage/images/signs/148.png"
  new_sign.name = "148"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 151
  new_sign.filepath = "/static/homePage/images/signs/151.png"
  new_sign.name = "151"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 152
  new_sign.filepath = "/static/homePage/images/signs/152b.png"
  new_sign.name = "152b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 165
  new_sign.filepath = "/static/homePage/images/signs/165.png"
  new_sign.name = "165"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 166
  new_sign.filepath = "/static/homePage/images/signs/166b.png"
  new_sign.name = "166b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 167
  new_sign.filepath = "/static/homePage/images/signs/167.png"
  new_sign.name = "167"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 170
  new_sign.filepath = "/static/homePage/images/signs/170.png"
  new_sign.name = "170"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 172
  new_sign.filepath = "/static/homePage/images/signs/172.png"
  new_sign.name = "172"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 173
  new_sign.filepath = "/static/homePage/images/signs/173.png"
  new_sign.name = "173"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 191
  new_sign.filepath = "/static/homePage/images/signs/191.png"
  new_sign.name = "191"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 203
  new_sign.filepath = "/static/homePage/images/signs/203.png"
  new_sign.name = "203"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 205
  new_sign.filepath = "/static/homePage/images/signs/205.png"
  new_sign.name = "205"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 206
  new_sign.filepath = "/static/homePage/images/signs/206.png"
  new_sign.name = "206"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 206
  new_sign.filepath = "/static/homePage/images/signs/206.png"
  new_sign.name = "206"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 207
  new_sign.filepath = "/static/homePage/images/signs/207.png"
  new_sign.name = "207"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 208
  new_sign.filepath = "/static/homePage/images/signs/208.png"
  new_sign.name = "208"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 211
  new_sign.filepath = "/static/homePage/images/signs/211.png"
  new_sign.name = "211"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 212
  new_sign.filepath = "/static/homePage/images/signs/212.png"
  new_sign.name = "212"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 214
  new_sign.filepath = "/static/homePage/images/signs/214.png"
  new_sign.name = "214"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 228
  new_sign.filepath = "/static/homePage/images/signs/228.png"
  new_sign.name = "228"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 229
  new_sign.filepath = "/static/homePage/images/signs/229.png"
  new_sign.name = "229"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 230
  new_sign.filepath = "/static/homePage/images/signs/230.png"
  new_sign.name = "230"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 231
  new_sign.filepath = "/static/homePage/images/signs/231.png"
  new_sign.name = "231"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 232
  new_sign.filepath = "/static/homePage/images/signs/232.png"
  new_sign.name = "232"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 280
  new_sign.filepath = "/static/homePage/images/signs/280.png"
  new_sign.name = "280"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 295
  new_sign.filepath = "/static/homePage/images/signs/295.png"
  new_sign.name = "295"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 296
  new_sign.filepath = "/static/homePage/images/signs/295ee.png"
  new_sign.name = "295ee"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 297
  new_sign.filepath = "/static/homePage/images/signs/295m.png"
  new_sign.name = "295m"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 298
  new_sign.filepath = "/static/homePage/images/signs/296.png"
  new_sign.name = "296"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 299
  new_sign.filepath = "/static/homePage/images/signs/297.png"
  new_sign.name = "297"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 300
  new_sign.filepath = "/static/homePage/images/signs/298.png"
  new_sign.name = "298"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 306
  new_sign.filepath = "/static/homePage/images/signs/306.png"
  new_sign.name = "306"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 307
  new_sign.filepath = "/static/homePage/images/signs/307.png"
  new_sign.name = "307"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 308
  new_sign.filepath = "/static/homePage/images/signs/308.png"
  new_sign.name = "308"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 309
  new_sign.filepath = "/static/homePage/images/signs/309.png"
  new_sign.name = "309"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 312
  new_sign.filepath = "/static/homePage/images/signs/312.png"
  new_sign.name = "312"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 313
  new_sign.filepath = "/static/homePage/images/signs/313.png"
  new_sign.name = "313"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 314
  new_sign.filepath = "/static/homePage/images/signs/314.png"
  new_sign.name = "314"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 318
  new_sign.filepath = "/static/homePage/images/signs/318.png"
  new_sign.name = "318"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 319
  new_sign.filepath = "/static/homePage/images/signs/319.png"
  new_sign.name = "319"
  new_sign.mimeType = "2"
  new_sign.save()


  new_sign = m.Sign()
  new_sign.id = 321
  new_sign.filepath = "/static/homePage/images/signs/321.png"
  new_sign.name = "321"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 322
  new_sign.filepath = "/static/homePage/images/signs/322.png"
  new_sign.name = "322"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 324
  new_sign.filepath = "/static/homePage/images/signs/324.png"
  new_sign.name = "324"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 328
  new_sign.filepath = "/static/homePage/images/signs/328.png"
  new_sign.name = "328"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 329
  new_sign.filepath = "/static/homePage/images/signs/329.png"
  new_sign.name = "329"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 330
  new_sign.filepath = "/static/homePage/images/signs/330.png"
  new_sign.name = "330"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 331
  new_sign.filepath = "/static/homePage/images/signs/331.png"
  new_sign.name = "331"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 332
  new_sign.filepath = "/static/homePage/images/signs/331e.png"
  new_sign.name = "331e"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 333
  new_sign.filepath = "/static/homePage/images/signs/333.png"
  new_sign.name = "333"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 334
  new_sign.filepath = "/static/homePage/images/signs/334.png"
  new_sign.name = "334"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 335
  new_sign.filepath = "/static/homePage/images/signs/335.png"
  new_sign.name = "335"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 339
  new_sign.filepath = "/static/homePage/images/signs/339.png"
  new_sign.name = "339"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 342
  new_sign.filepath = "/static/homePage/images/signs/342.png"
  new_sign.name = "342"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 343
  new_sign.filepath = "/static/homePage/images/signs/343.png"
  new_sign.name = "343"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 349
  new_sign.filepath = "/static/homePage/images/signs/349.png"
  new_sign.name = "349"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 353
  new_sign.filepath = "/static/homePage/images/signs/353a.png"
  new_sign.name = "353a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 354
  new_sign.filepath = "/static/homePage/images/signs/354a.png"
  new_sign.name = "354a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 355
  new_sign.filepath = "/static/homePage/images/signs/354b.png"
  new_sign.name = "354b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 366
  new_sign.filepath = "/static/homePage/images/signs/366.png"
  new_sign.name = "366"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 367
  new_sign.filepath = "/static/homePage/images/signs/367.png"
  new_sign.name = "367"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 371
  new_sign.filepath = "/static/homePage/images/signs/371.png"
  new_sign.name = "371"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 372
  new_sign.filepath = "/static/homePage/images/signs/372.png"
  new_sign.name = "372"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 374
  new_sign.filepath = "/static/homePage/images/signs/374.png"
  new_sign.name = "374"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 376
  new_sign.filepath = "/static/homePage/images/signs/376.png"
  new_sign.name = "376"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 378
  new_sign.filepath = "/static/homePage/images/signs/378a.png"
  new_sign.name = "378a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 381
  new_sign.filepath = "/static/homePage/images/signs/381.png"
  new_sign.name = "381"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 383
  new_sign.filepath = "/static/homePage/images/signs/383.png"
  new_sign.name = "383"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 384
  new_sign.filepath = "/static/homePage/images/signs/384.png"
  new_sign.name = "384"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 395
  new_sign.filepath = "/static/homePage/images/signs/395a.png"
  new_sign.name = "395a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 396
  new_sign.filepath = "/static/homePage/images/signs/396a.png"
  new_sign.name = "396a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 397
  new_sign.filepath = "/static/homePage/images/signs/396b.png"
  new_sign.name = "396b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 398
  new_sign.filepath = "/static/homePage/images/signs/398.png"
  new_sign.name = "398"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 399
  new_sign.filepath = "/static/homePage/images/signs/399.png"
  new_sign.name = "399"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 401
  new_sign.filepath = "/static/homePage/images/signs/401.png"
  new_sign.name = "401"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 406
  new_sign.filepath = "/static/homePage/images/signs/406.png"
  new_sign.name = "406"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 411
  new_sign.filepath = "/static/homePage/images/signs/411.png"
  new_sign.name = "411"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 420
  new_sign.filepath = "/static/homePage/images/signs/420.png"
  new_sign.name = "420"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 427
  new_sign.filepath = "/static/homePage/images/signs/427.png"
  new_sign.name = "427"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 429
  new_sign.filepath = "/static/homePage/images/signs/429.png"
  new_sign.name = "429"
  new_sign.mimeType = "2"
  new_sign.save()


  new_sign = m.Sign()
  new_sign.id = 433
  new_sign.filepath = "/static/homePage/images/signs/433.png"
  new_sign.name = "433"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 435
  new_sign.filepath = "/static/homePage/images/signs/435.png"
  new_sign.name = "435"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 437
  new_sign.filepath = "/static/homePage/images/signs/437.png"
  new_sign.name = "437"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 441
  new_sign.filepath = "/static/homePage/images/signs/441.png"
  new_sign.name = "441"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 446
  new_sign.filepath = "/static/homePage/images/signs/446.png"
  new_sign.name = "446"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 449
  new_sign.filepath = "/static/homePage/images/signs/449.png"
  new_sign.name = "449"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 451
  new_sign.filepath = "/static/homePage/images/signs/451.png"
  new_sign.name = ""
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 454
  new_sign.filepath = "/static/homePage/images/signs/454.png"
  new_sign.name = "454"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 455
  new_sign.filepath = "/static/homePage/images/signs/455.png"
  new_sign.name = "455"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 457
  new_sign.filepath = "/static/homePage/images/signs/457.png"
  new_sign.name = "457"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 461
  new_sign.filepath = "/static/homePage/images/signs/461.png"
  new_sign.name = "461"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 468
  new_sign.filepath = "/static/homePage/images/signs/468.png"
  new_sign.name = "468"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 471
  new_sign.filepath = "/static/homePage/images/signs/471.png"
  new_sign.name = "471"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 472
  new_sign.filepath = "/static/homePage/images/signs/472.png"
  new_sign.name = "472"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 473
  new_sign.filepath = "/static/homePage/images/signs/473.png"
  new_sign.name = "473"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 475
  new_sign.filepath = "/static/homePage/images/signs/475.png"
  new_sign.name = "475"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 480
  new_sign.filepath = "/static/homePage/images/signs/480.png"
  new_sign.name = "480"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 481
  new_sign.filepath = "/static/homePage/images/signs/481.png"
  new_sign.name = "481"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 482
  new_sign.filepath = "/static/homePage/images/signs/482.png"
  new_sign.name = "482"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 532
  new_sign.filepath = "/static/homePage/images/signs/532.png"
  new_sign.name = "532"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 535
  new_sign.filepath = "/static/homePage/images/signs/535.png"
  new_sign.name = "535"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 536
  new_sign.filepath = "/static/homePage/images/signs/536a.png"
  new_sign.name = "536a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 537
  new_sign.filepath = "/static/homePage/images/signs/536b.png"
  new_sign.name = ""
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 538
  new_sign.filepath = "/static/homePage/images/signs/537.png"
  new_sign.name = "537"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 539
  new_sign.filepath = "/static/homePage/images/signs/539.png"
  new_sign.name = "539"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 554
  new_sign.filepath = "/static/homePage/images/signs/554.png"
  new_sign.name = "554"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 555
  new_sign.filepath = "/static/homePage/images/signs/555.png"
  new_sign.name = "555"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 556
  new_sign.filepath = "/static/homePage/images/signs/556.png"
  new_sign.name = "556"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 557
  new_sign.filepath = "/static/homePage/images/signs/557.png"
  new_sign.name = "557"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 558
  new_sign.filepath = "/static/homePage/images/signs/558.png"
  new_sign.name = "558"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 559
  new_sign.filepath = "/static/homePage/images/signs/559.png"
  new_sign.name = "559"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 562
  new_sign.filepath = "/static/homePage/images/signs/562.png"
  new_sign.name = "562"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 564
  new_sign.filepath = "/static/homePage/images/signs/564.png"
  new_sign.name = "564"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 565
  new_sign.filepath = "/static/homePage/images/signs/565.png"
  new_sign.name = "565"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 570
  new_sign.filepath = "/static/homePage/images/signs/570.png"
  new_sign.name = "570"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 571
  new_sign.filepath = "/static/homePage/images/signs/571.png"
  new_sign.name = "571"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 572
  new_sign.filepath = "/static/homePage/images/signs/572.png"
  new_sign.name = "572"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 573
  new_sign.filepath = "/static/homePage/images/signs/573.png"
  new_sign.name = "573"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 575
  new_sign.filepath = "/static/homePage/images/signs/575.png"
  new_sign.name = "575"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 579
  new_sign.filepath = "/static/homePage/images/signs/579.png"
  new_sign.name = "579"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 586
  new_sign.filepath = "/static/homePage/images/signs/586.png"
  new_sign.name = "586"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 589
  new_sign.filepath = "/static/homePage/images/signs/589.png"
  new_sign.name = "589"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 591
  new_sign.filepath = "/static/homePage/images/signs/591.png"
  new_sign.name = "591"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 593
  new_sign.filepath = "/static/homePage/images/signs/593.png"
  new_sign.name = "593"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 595
  new_sign.filepath = "/static/homePage/images/signs/595.png"
  new_sign.name = "595"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 597
  new_sign.filepath = "/static/homePage/images/signs/597a.png"
  new_sign.name = "597a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 598
  new_sign.filepath = "/static/homePage/images/signs/597b.png"
  new_sign.name = "597b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 599
  new_sign.filepath = "/static/homePage/images/signs/598a.png"
  new_sign.name = "598a"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 600
  new_sign.filepath = "/static/homePage/images/signs/598b.png"
  new_sign.name = "598b"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 601
  new_sign.filepath = "/static/homePage/images/signs/598c.png"
  new_sign.name = "598c"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 602
  new_sign.filepath = "/static/homePage/images/signs/598d.png"
  new_sign.name = "598d"
  new_sign.mimeType = "2"
  new_sign.save()

  new_sign = m.Sign()
  new_sign.id = 603
  new_sign.filepath = "/static/homePage/images/signs/598e.png"
  new_sign.name = "598e"
  new_sign.mimeType = "2"
  new_sign.save()

  tvars = {
  }
  return templater.render_to_response(request, 'login.html', tvars)
