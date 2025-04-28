from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <html>
        <head>
            <title>Toko Buku Online</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f5f5f5;
                    padding: 20px;
                    text-align: center;
                }
                .products {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                }
                .product {
                    background: white;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    margin: 15px;
                    padding: 15px;
                    width: 220px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    transition: transform 0.2s;
                }
                .product:hover {
                    transform: translateY(-5px);
                }
                .product img {
                    width: 100%;
                    height: 250px;
                    object-fit: cover;
                    border-radius: 4px;
                }
                .product h3 {
                    font-size: 18px;
                    margin: 10px 0 5px 0;
                }
                .product p {
                    margin: 5px 0;
                    font-size: 15px;
                    color: #555;
                }
                .rating {
                    color: gold;
                    font-size: 18px;
                }
                .button {
                    display: inline-block;
                    margin-top: 30px;
                    padding: 12px 25px;
                    background-color: #397298;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 18px;
                    font-weight: bold;
                    box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                }
                .button:hover {
                    background-color: #2f5d7a; 
                    transform: scale(1.05);
                }
            </style>
        </head>
        <body>
            <nav style="background-color: #397298; padding: 15px 0; margin-bottom: 30px;">
            <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: center;">
                <a href="/" style="color: white; text-decoration: none; margin: 0 20px; font-weight: bold;">Beranda</a>
                <a href="/produk/" style="color: white; text-decoration: none; margin: 0 20px; font-weight: bold;">Produk</a>
                <a href="/kontak/" style="color: white; text-decoration: none; margin: 0 20px; font-weight: bold;">Kontak</a>
                <a href="/tentang/" style="color: white; text-decoration: none; margin: 0 20px; font-weight: bold;">Tentang</a>
            </div>
            </nav>
            <h1>Selamat Datang di Toko Buku Online!</h1>
            <div class="products">
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/91bYsX41DVL.jpg" alt="Atomic Habits">
                    <h3>Atomic Habits</h3>
                    <p>Rp 120.000</p>
                    <div class="rating">★★★★★</div>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/71g2ednj0JL.jpg" alt="The Psychology of Money">
                    <h3>The Psychology of Money</h3>
                    <p>Rp 150.000</p>
                    <div class="rating">★★★★★</div>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg" alt="The Alchemist">
                    <h3>The Alchemist</h3>
                    <p>Rp 100.000</p>
                    <div class="rating">★★★★☆</div>
                </div>
            </div>
            <br>
            <a href="/produk/" class="button">Lihat Semua Buku</a>
        </body>
    </html>
    """)

def produk_view(request):
    return HttpResponse("""
    <html>
        <head>
            <title>Daftar Produk</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f5f5f5;
                    padding: 20px;
                    text-align: center;
                }
                .product-list {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                }
                .product {
                    width: 200px;
                    background: white;
                    padding: 15px;
                    border-radius: 10px;
                    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    transition: transform 0.3s ease;
                }
                .product:hover {
                    transform: translateY(-5px); /* Efek hover */
                }
                .product img {
                    width: 100%;
                    height: 250px;
                    object-fit: cover;
                    border-radius: 8px;
                }
                .product h3 {
                    font-size: 16px;
                    margin: 10px 0;
                    height: 48px;
                    overflow: hidden;
                }
                .product p {
                    color: #333;
                    font-size: 16px;
                    margin: 8px 0;
                }
                .rating {
                    color: gold;
                    font-size: 16px;
                    margin: 5px 0;
                }
                .button {
                    margin-top: 10px;
                    padding: 8px 15px;
                    background-color: #397298;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: bold;
                    transition: background-color 0.3s ease;
                }
                .button:hover {
                    background-color: #2f5d7a;
                }
            </style>
        </head>
        <body>
            <h1>Daftar Produk</h1>
            <div class="product-list">
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/91bYsX41DVL.jpg" alt="Atomic Habits">
                    <h3>Atomic Habits</h3>
                    <div class="rating">★★★★★</div>
                    <p>Rp 120.000</p>
                    <a href="/produk/1/" class="button">Lihat Detail</a>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/71UwSHSZRnS.jpg" alt="The Psychology of Money">
                    <h3>The Power of Your Subconscious Mind</h3>
                    <div class="rating">★★★★☆</div>
                    <p>Rp 150.000</p>
                    <a href="/produk/2/" class="button">Lihat Detail</a>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/81bsw6fnUiL.jpg" alt="Rich Dad Poor Dad">
                    <h3>Rich Dad Poor Dad</h3>
                    <div class="rating">★★★★☆</div>
                    <p>Rp 135.000</p>
                    <a href="/produk/3/" class="button">Lihat Detail</a>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/713jIoMO3UL.jpg" alt="Sapiens">
                    <h3>Sapiens: A Brief History of Humankind</h3>
                    <div class="rating">★★★★☆</div>
                    <p>Rp 180.000</p>
                    <a href="/produk/4/" class="button">Lihat Detail</a>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/81QpkIctqPL.jpg" alt="The Subtle Art of Not Giving a F*ck">
                    <h3>The Subtle Art of Not Giving a F*ck</h3>
                    <div class="rating">★★★★☆</div>
                    <p>Rp 140.000</p>
                    <a href="/produk/5/" class="button">Lihat Detail</a>
                </div>
                <div class="product">
                    <img src="https://m.media-amazon.com/images/I/71g2ednj0JL.jpg" alt="Start with Why">
                    <h3>The Psychology of Money</h3>
                    <div class="rating">★★★★★</div>
                    <p>Rp 160.000</p>
                    <a href="/produk/6/" class="button">Lihat Detail</a>
                </div>
            </div>
        </body>
    </html>
    """)

def product_detail(request, product_id):
    # Data produk (biasanya ini akan diambil dari database)
    products = {
        1: {
            "title": "Atomic Habits",
            "price": "Rp 120.000",
            "rating": "★★★★★",
            "description": "Buku Atomic Habits mengajarkan cara membangun kebiasaan baik dan menghilangkan kebiasaan buruk melalui pendekatan ilmiah yang mudah dipahami.",
            "author": "James Clear",
            "pages": "320 halaman",
            "language": "Bahasa Indonesia",
            "isbn": "978-602-291-704-9",
            "image": "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg"
        },
        2: {
            "title": "The Psychology of Money",
            "price": "Rp 150.000",
            "rating": "★★★★★",
            "description": "Buku ini mengeksplorasi cara aneh orang berpikir tentang uang dan mengajarkan pelajaran tentang kekayaan, keserakahan, dan kebahagiaan.",
            "author": "Morgan Housel",
            "pages": "256 halaman",
            "language": "Bahasa Indonesia",
            "isbn": "978-602-064-951-1",
            "image": "https://m.media-amazon.com/images/I/71g2ednj0JL.jpg"
        },
        3: {
            "title": "The Alchemist",
            "price": "Rp 100.000",
            "rating": "★★★★☆",
            "description": "Novel inspiratif tentang perjalanan seorang gembala muda bernama Santiago dalam mencari harta karun dan menemukan makna hidup sejati.",
            "author": "Paulo Coelho",
            "pages": "208 halaman",
            "language": "Bahasa Indonesia",
            "isbn": "978-602-03-2876-5",
            "image": "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg"
        }
    }
    
    product = products.get(product_id)
    
    if not product:
        return HttpResponse("Produk tidak ditemukan")
    
    return HttpResponse(f"""
    <html>
        <head>
            <title>{product['title']} - Toko Buku Online</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }}
                .container {{
                    max-width: 1000px;
                    margin: 20px auto;
                    padding: 20px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 0 15px rgba(0,0,0,0.1);
                }}
                .product-detail {{
                    display: flex;
                    gap: 30px;
                }}
                .product-image {{
                    flex: 1;
                }}
                .product-image img {{
                    width: 100%;
                    max-width: 400px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }}
                .product-info {{
                    flex: 2;
                }}
                h1 {{
                    color: #397298;
                    margin-top: 0;
                }}
                .price {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #e74c3c;
                    margin: 15px 0;
                }}
                .rating {{
                    color: gold;
                    font-size: 20px;
                    margin: 10px 0;
                }}
                .description {{
                    margin: 20px 0;
                    line-height: 1.6;
                }}
                .details {{
                    background: #f9f9f9;
                    padding: 15px;
                    border-radius: 8px;
                    margin: 20px 0;
                }}
                .details table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                .details td {{
                    padding: 8px 0;
                    border-bottom: 1px solid #eee;
                }}
                .details td:first-child {{
                    font-weight: bold;
                    width: 150px;
                }}
                .button {{
                    display: inline-block;
                    padding: 12px 25px;
                    background-color: #397298;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: bold;
                    margin-top: 10px;
                    transition: background-color 0.3s;
                }}
                .button:hover {{
                    background-color: #2f5d7a;
                }}
                .back-link {{
                    display: inline-block;
                    margin-top: 20px;
                    color: #397298;
                    text-decoration: none;
                }}
                .back-link:hover {{
                    text-decoration: underline;
                }}
            </style>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        </head>
        <body>
            <div class="container">
                <a href="/produk/" class="back-link"><i class="fas fa-arrow-left"></i> Kembali ke Daftar Produk</a>
                
                <div class="product-detail">
                    <div class="product-image">
                        <img src="{product['image']}" alt="{product['title']}">
                    </div>
                    <div class="product-info">
                        <h1>{product['title']}</h1>
                        <div class="rating">{product['rating']}</div>
                        <div class="price">{product['price']}</div>
                        
                        <div class="description">
                            <p>{product['description']}</p>
                        </div>
                        
                        <a href="#" class="button"><i class="fas fa-shopping-cart"></i> Tambah ke Keranjang</a>
                        <a href="#" class="button" style="background-color: #27ae60; margin-left: 10px;"><i class="fas fa-bolt"></i> Beli Sekarang</a>
                        
                        <div class="details">
                            <h3>Detail Produk</h3>
                            <table>
                                <tr>
                                    <td>Penulis</td>
                                    <td>{product['author']}</td>
                                </tr>
                                <tr>
                                    <td>Jumlah Halaman</td>
                                    <td>{product['pages']}</td>
                                </tr>
                                <tr>
                                    <td>Bahasa</td>
                                    <td>{product['language']}</td>
                                </tr>
                                <tr>
                                    <td>ISBN</td>
                                    <td>{product['isbn']}</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
                
                <div style="margin-top: 40px;">
                    <h3>Ulasan Pelanggan</h3>
                    <div style="background: #f9f9f9; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                        <div style="display: flex; justify-content: space-between;">
                            <strong>Andi Pratama</strong>
                            <div style="color: gold;">★★★★★</div>
                        </div>
                        <p style="margin-top: 5px;">Buku ini sangat menginspirasi! Saya bisa menerapkan tips membangun kebiasaan baik dengan mudah.</p>
                        <small style="color: #777;">12 Maret 2023</small>
                    </div>
                    <div style="background: #f9f9f9; padding: 15px; border-radius: 8px;">
                        <div style="display: flex; justify-content: space-between;">
                            <strong>Budi Santoso</strong>
                            <div style="color: gold;">★★★★☆</div>
                        </div>
                        <p style="margin-top: 5px;">Kontennya bagus, tapi pengiriman agak lama. Overall puas dengan produknya.</p>
                        <small style="color: #777;">28 Februari 2023</small>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """)

def kontak(request):
    return HttpResponse("""
    <html>
        <head>
            <title>Kontak Kami - Toko Buku Online</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #397298;
                    text-align: center;
                    margin-bottom: 30px;
                }
                .contact-info {
                    margin-bottom: 30px;
                }
                .contact-info div {
                    margin-bottom: 15px;
                    display: flex;
                    align-items: center;
                }
                .contact-info i {
                    font-size: 24px;
                    margin-right: 15px;
                    color: #397298;
                    width: 30px;
                    text-align: center;
                }
                .contact-form input,
                .contact-form textarea {
                    width: 100%;
                    padding: 12px;
                    margin-bottom: 15px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    font-family: inherit;
                }
                .contact-form textarea {
                    height: 150px;
                }
                .submit-btn {
                    background-color: #397298;
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                    transition: background-color 0.3s;
                }
                .submit-btn:hover {
                    background-color: #2f5d7a;
                }
                .back-link {
                    display: inline-block;
                    margin-top: 20px;
                    color: #397298;
                    text-decoration: none;
                }
                .back-link:hover {
                    text-decoration: underline;
                }
            </style>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        </head>
        <body>
            <div class="container">
                <h1>Hubungi Kami</h1>
                
                <div class="contact-info">
                    <div>
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Jl. Fatahillah No. 123, Banda Aceh, Indonesia</span>
                    </div>
                    <div>
                        <i class="fas fa-phone"></i>
                        <span>+62 123 4567 890</span>
                    </div>
                    <div>
                        <i class="fas fa-envelope"></i>
                        <span>info@tokobukuonline.com</span>
                    </div>
                    <div>
                        <i class="fas fa-clock"></i>
                        <span>Buka Senin-Jumat: 09.00 - 17.00 WIB</span>
                    </div>
                </div>
                
                <h2>Kirim Pesan</h2>
                <form class="contact-form">
                    <input type="text" placeholder="Nama Anda" required>
                    <input type="email" placeholder="Email Anda" required>
                    <input type="text" placeholder="Subjek">
                    <textarea placeholder="Pesan Anda" required></textarea>
                    <button type="submit" class="submit-btn">Kirim Pesan</button>
                </form>
                
                <a href="/" class="back-link">← Kembali ke Beranda</a>
            </div>
        </body>
    </html>
    """)

def tentang(request):
    return HttpResponse("""
    <html>
        <head>
            <title>Tentang Kami - Toko Buku Online</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                    color: #333;
                }
                .container {
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                }
                header {
                    background-color: #397298;
                    color: white;
                    padding: 30px 0;
                    text-align: center;
                    margin-bottom: 40px;
                }
                h1 {
                    margin: 0;
                    font-size: 2.5em;
                }
                h2 {
                    color: #397298;
                    border-bottom: 2px solid #397298;
                    padding-bottom: 10px;
                    margin-top: 30px;
                }
                .about-content {
                    background: white;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 0 15px rgba(0,0,0,0.1);
                }
                .mission-vision {
                    display: flex;
                    gap: 20px;
                    margin: 30px 0;
                }
                .mission, .vision {
                    flex: 1;
                    background: #f9f9f9;
                    padding: 20px;
                    border-radius: 8px;
                    border-left: 4px solid #397298;
                }
                .team {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                    justify-content: center;
                    margin: 30px 0;
                }
                .team-member {
                    width: 200px;
                    text-align: center;
                }
                .team-member img {
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    object-fit: cover;
                    border: 3px solid #397298;
                    margin-bottom: 15px;
                }
                .values {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 15px;
                    justify-content: center;
                }
                .value-item {
                    background: #397298;
                    color: white;
                    padding: 15px;
                    border-radius: 8px;
                    width: 200px;
                    text-align: center;
                }
                .value-item i {
                    font-size: 2em;
                    margin-bottom: 10px;
                    display: block;
                }
                .back-link {
                    display: inline-block;
                    margin-top: 20px;
                    color: #397298;
                    text-decoration: none;
                    font-weight: bold;
                }
                .back-link:hover {
                    text-decoration: underline;
                }
            </style>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        </head>
        <body>
            <header>
                <div class="container">
                    <h1>Tentang Toko Buku Online Kami</h1>
                    <p>Menyediakan pengetahuan dan inspirasi melalui buku-buku berkualitas</p>
                </div>
            </header>
            
            <div class="container">
                <div class="about-content">
                    <h2>Sejarah Kami</h2>
                    <p>Toko Buku Online memiliki misi untuk menyebarkan pengetahuan dan inspirasi kepada masyarakat Indonesia. Bermula dari sebuah toko kecil di Banda Aceh, kami telah berkembang menjadi salah satu platform buku online terpercaya di Indonesia.</p>
                    <p>Dengan lebih dari 10.000 judul buku dari berbagai genre dan penerbit ternama, kami bangga dapat melayani ribuan pelanggan setiap bulannya. Komitmen kami terhadap kualitas dan pelayanan telah menjadikan kami pilihan utama para pecinta buku.</p>
                    
                    <div class="mission-vision">
                        <div class="mission">
                            <h3><i class="fas fa-bullseye"></i> Misi Kami</h3>
                            <p>Menyediakan akses mudah terhadap buku-buku berkualitas untuk meningkatkan literasi masyarakat Indonesia. Kami berkomitmen untuk menjadi jembatan antara pembaca dengan pengetahuan dan inspirasi melalui koleksi buku yang beragam dan relevan.</p>
                        </div>
                        <div class="vision">
                            <h3><i class="fas fa-eye"></i> Visi Kami</h3>
                            <p>Menjadi platform buku online terdepan di Indonesia yang tidak hanya menjual buku, tetapi juga menumbuhkan komunitas pembaca yang kritis dan inspiratif. Kami ingin menciptakan generasi Indonesia yang cerdas dan berwawasan luas.</p>
                        </div>
                    </div>
                    
                    <h2>Nilai-Nilai Kami</h2>
                    <div class="values">
                        <div class="value-item">
                            <i class="fas fa-book-open"></i>
                            <h3>Literasi</h3>
                            <p>Kami percaya buku adalah jendela dunia dan alat untuk pemberdayaan</p>
                        </div>
                        <div class="value-item">
                            <i class="fas fa-hand-holding-heart"></i>
                            <h3>Integritas</h3>
                            <p>Transparansi dan kejujuran dalam setiap transaksi dan interaksi</p>
                        </div>
                        <div class="value-item">
                            <i class="fas fa-lightbulb"></i>
                            <h3>Inovasi</h3>
                            <p>Terus berkembang untuk memberikan pengalaman berbelanja terbaik</p>
                        </div>
                        <div class="value-item">
                            <i class="fas fa-users"></i>
                            <h3>Komunitas</h3>
                            <p>Membangun jaringan pecinta buku yang saling mendukung</p>
                        </div>
                    </div>
                    
                    <h2>Tim Kami</h2>
                    <p>Di balik Toko Buku Online, ada tim yang penuh semangat dan berdedikasi tinggi yang bekerja keras untuk memastikan Anda mendapatkan pengalaman berbelanja buku yang menyenangkan.</p>
                    
                    <div class="team">
                        <div class="team-member">
                            <img src="https://randomuser.me/api/portraits/women/65.jpg" alt="Direktur">
                            <h3>Meutia Aini</h3>
                            <p>Direktur</p>
                        </div>
                        <div class="team-member">
                            <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Manajer">
                            <h3>Iffatun Nisa</h3>
                            <p>Manajer Operasional</p>
                        </div>
                        <div class="team-member">
                            <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Kurator">
                            <h3>M. Syahidal Akbar Zas</h3>
                            <p>Kurator Buku</p>
                        </div>
                        <div class="team-member">
                            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="Customer Service">
                            <h3>Dowoon</h3>
                            <p>Layanan Pelanggan</p>
                        </div>
                    </div>
                    
                    <h2>Komitmen Kami</h2>
                    <p>Kami tidak hanya menjual buku, tetapi juga berkomitmen untuk:</p>
                    <ul>
                        <li>Menyediakan buku-buku asli dan berkualitas tinggi</li>
                        <li>Memberikan pelayanan pelanggan yang ramah dan responsif</li>
                        <li>Menjaga harga yang kompetitif dan terjangkau</li>
                        <li>Mengemas buku dengan aman untuk pengiriman</li>
                        <li>Menyediakan rekomendasi buku yang personal</li>
                    </ul>
                    
                    <p>Terima kasih telah menjadi bagian dari perjalanan kami. Setiap pembelian Anda mendukung ekosistem literasi di Indonesia.</p>
                    
                    <a href="/" class="back-link"><i class="fas fa-arrow-left"></i> Kembali ke Beranda</a>
                </div>
            </div>
        </body>
    </html>
    """)

