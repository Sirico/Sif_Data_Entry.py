import flaskblog

# Varible to store the choices for the dropdown menu using popular sportswear brands


Brand = [
    ('*Select a brand'),
    ('Nike'),
    ('Adidas'),
    ('Asics'),
    ('Reebok'),
    ('Puma'),
    ('Under Armour'),
    ('Vans'),
    ('Converse'),
    ('New Balance'),
    ('Victory'),
    ('Skechers'),
    ('Crocs'),
    ('J.Crew'),
    ('Tommy Hilfiger'),
    ('Levi Strauss & Co'), ]
Brand.sort()
Colour = [
    ('*Select a colour'),
    ('Black'),
    ('White'),
    ('Red'),
    ('Blue'),
    ('Green'),
    ('Yellow'),
    ('Orange'),
    ('Purple'),
    ('Pink'),
    ('Brown'),
    ('Grey'),
    ('Silver'),
    ('Gold'),
    ('Other')]
Colour.sort()

Country = ['*Select a Country', 'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa',
           'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina',
           'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
           'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, '
                                                                                     'Plurinational State of',
           'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana',
           'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria',
           'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
           'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands',
           'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica',
           "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti',
           'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', ''
                                                                                                                'Estonia',
           'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
           'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
           'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
           'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)',
           'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq',
           'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
           'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan',
           "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
           'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
           'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
           'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
           'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia',
           'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands',
           'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea',
           'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion',
           'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy',
           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia',
           'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa',
           'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
           'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
           'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
           'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
           'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo',
           'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands',
           'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
           'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu',
           'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British',
           'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
Country.sort()

Adults_Footwear = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Kids_Footwear = ['1k', '1.5k', '2k', '2.5k', '3k', '3.5k', '4k', '4.5k', '5k', '5.5k', '6k', '6.5k', '7k', '7.5k', '8k',
                 '8.5k', '9k', '9.5k', '10k', '10.5k', '11k', '11.5k', '12k', '12.5k', '13k', '13.5k', '1', '1.5', '2',
                 '2.5',
                 '3', '3.5', '4', '4.5', '5', '5.5', '6', '6.5']

Adults_Clothing = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']

Kids_Clothing = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']

Accessories_sizes = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL', 'Universal fit']

Type_Footwear = ['*Select type of footwear', 'Trainers', 'Canvas & Plimsoles', 'Flip-Flops & Slides', 'Running Shoes',
                 'Football Boots', 'Shoes',
                 'Boots', 'Basketball']
Type_Footwear.sort()

Type_Clothing = ['*Select Type of clothing', 'Hoodies', 'Track Pants', 'Vests', 'Tees & Tops', 'Tracksuits',
                 'Sweatshirts', 'Jackets & Gilets',
                 'Trousers', 'Jeans & Chinos', 'Shorts', 'Swimwear', 'Football', 'Baselayers', 'Polo Shirts',
                 'Socks & Underwear', 'Formal Shirts', 'Coats', 'Sets', 'Workwear', 'Blazers']
Type_Clothing.sort()

Type_Accessories = ['*Select type of accessory', 'Bags', 'Caps', 'Beanies', 'Gloves & Scarves', 'Watches',
                    'Sunglasses', 'Wallets', 'Other', 'Belts',
                    'Fragrances', 'Swimming', 'Football Accessories', 'Ties']
Type_Accessories.sort()

Type_Closure = ['*Select type of closure', 'Zip', 'Button', 'Popper', 'Clasp', 'Magnetic', 'Other']
