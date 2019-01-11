import fresh_tomatoes
import media
Titanic = media.Cinema("Titanic"," Love Story in a sinking ship",
                            "https://i.pinimg.com/originals/43/da/e0/43dae080442402c7fab4c93603fc74bf.jpg",
                            "https://youtu.be/zCy5WQ9S4c0")
#print(titanic.storyline)
Twilight = media.Cinema("Twilight"," Love story between vampire&human",
                        "https://i.pinimg.com/originals/ce/de/c0/cedec0e7657d62e4a39d4af507f10d01.jpg",
                        "https://youtu.be/QDRLSqm_WVg")
#print(twilight.storyline)
#twilight.show_trailer()
BossBaby = media.Cinema("BossBaby","About boss baby",
                            "https://images-na.ssl-images-amazon.com/images/I/61wd2PsE8HL._SY606_.jpg",
                            "https://youtu.be/k397HRbTtWI")
Bangloredays= media.Cinema("Banglore days","All about Friendship ",
                            "https://s3.ap-southeast-1.amazonaws.com/cdn.deccanchronicle.com/sites/default/files/Bangalore%20Days_0_0.jpg",
                            "https://youtu.be/Gdzif0Px_qY")
OruAdaarLove= media.Cinema("Oru Adaar Love","Beautiful love story in a school",
                            "https://www.filmibeat.com/img/2018/09/malayalamsong-1537880107.jpg",
                            "https://youtu.be/W0fKl43QmIE")
Aanandam= media.Cinema("Aanandam","Journey of a college students",
                            "https://i.ytimg.com/vi/ojyKxuuOdSU/maxresdefault.jpg",
                            "https://youtu.be/9B1SDMwQRXk")
movies= [Titanic,Twilight,BossBaby,Bangloredays,OruAdaarLove,Aanandam]
fresh_tomatoes.open_movies_page(movies)
