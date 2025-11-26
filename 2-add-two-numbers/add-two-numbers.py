class Solution(object):
    def addTwoNumbers(self, l1, l2):

        yeni_liste_basi = ListNode(0)
        gezici = yeni_liste_basi
        elde = 0

        while l1 is not None or l2 is not None or elde != 0:

            deger1 = l1.val if l1 is not None else 0
            deger2 = l2.val if l2 is not None else 0

            toplam = deger1 + deger2 + elde
            
            # Yeni elde varı hesapla
            elde = toplam // 10
            
            # Sonuç basamağını bul 
            sonuc_basamagi = toplam % 10

            # Yeni düğümü oluştur ve gezicinin sonrasına ekle
            gezici.next = ListNode(sonuc_basamagi) 
            
            # Geziciyi yeni eklenen düğüme taşı
            gezici = gezici.next

            # Listeleri bir sonraki basamağa ekle
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return yeni_liste_basi.next