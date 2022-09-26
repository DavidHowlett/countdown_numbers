test_data = [
    ([6, 2, 9, 4, 25, 8], 200),
    ([7, 25, 2, 8, 1, 7], 161),
    ([10, 6, 4, 75, 9, 7], 306),
    ([6, 50, 9, 5, 7, 3], 112),
    ([10, 75, 5, 9, 3, 1], 585),
    ([9, 8, 4, 5, 100, 10], 550),
    ([7, 2, 50, 2, 100, 5], 455),
    ([7, 50, 5, 10, 3, 2], 505),
    ([5, 6, 50, 75, 3, 2], 108),
    ([8, 100, 6, 1, 3, 5], 796),
    ([4, 3, 25, 3, 9, 9], 135),
    ([3, 5, 1, 9, 6, 8], 264),
    ([1, 7, 9, 2, 8, 100], 157),
    ([10, 4, 5, 7, 9, 2], 121),
    ([4, 6, 7, 2, 5, 75], 290),
    ([8, 7, 9, 10, 75, 6], 149),
    ([10, 1, 8, 9, 100, 7], 899),
    ([25, 5, 9, 1, 3, 6], 158),
    ([6, 8, 5, 3, 5, 7], 375),
    ([4, 10, 8, 3, 9, 10], 238),
    ([1, 25, 2, 8, 6, 4], 193),
    ([8, 1, 3, 100, 6, 5], 576),
    ([5, 1, 3, 8, 10, 100], 972),
    ([5, 4, 9, 10, 6, 1], 128),
    ([8, 10, 5, 7, 50, 6], 266),
    ([100, 1, 8, 2, 5, 7], 694),
    ([10, 8, 9, 3, 100, 6], 372),
    ([6, 50, 2, 25, 5, 9], 410),
    ([8, 3, 50, 5, 9, 4], 226),
    ([3, 4, 3, 7, 6, 4], 558),
    ([10, 3, 3, 1, 4, 10], 363),
    ([3, 10, 9, 8, 1, 2], 643),
    ([9, 1, 75, 2, 4, 1], 782),
    ([6, 4, 4, 8, 5, 3], 552),
    ([4, 9, 2, 4, 5, 5], 451),
    ([10, 2, 3, 9, 6, 5], 173),
    ([4, 3, 50, 7, 4, 2], 406),
    ([6, 4, 3, 1, 100, 6], 544),
    ([2, 5, 6, 3, 7, 4], 116),
    ([10, 6, 3, 6, 2, 25], 283),
    ([1, 10, 100, 7, 6, 5], 221),
    ([2, 8, 1, 7, 2, 10], 109),
    ([10, 5, 1, 2, 7, 7], 276),
    ([6, 4, 10, 7, 9, 75], 698),
    ([5, 2, 3, 3, 75, 1], 332),
    ([3, 3, 6, 4, 100, 10], 373),
    ([7, 9, 3, 9, 2, 7], 738),
    ([100, 1, 6, 50, 10, 7], 138),
    ([1, 75, 6, 3, 2, 8], 258),
    ([4, 75, 7, 10, 25, 6], 976),
    ([10, 9, 6, 1, 2, 3], 663),
    ([75, 5, 9, 6, 1, 6], 185),
    ([1, 6, 9, 5, 100, 7], 380),
    ([2, 3, 8, 10, 1, 75], 314),
    ([8, 9, 1, 2, 8, 100], 413),
    ([6, 100, 8, 1, 4, 1], 583),
    ([5, 25, 6, 5, 9, 7], 343),
    ([9, 75, 2, 6, 9, 4], 338),
    ([2, 6, 10, 50, 2, 7], 173),
    ([9, 7, 4, 8, 7, 10], 555),
    ([3, 5, 50, 8, 9, 2], 296),
    ([4, 4, 5, 6, 10, 8], 812),
    ([5, 10, 4, 6, 9, 8], 844),
    ([1, 50, 7, 3, 2, 7], 846),
    ([4, 10, 3, 75, 7, 1], 583),
    ([10, 8, 25, 5, 2, 7], 148),
    ([5, 4, 100, 1, 3, 9], 183),
    ([5, 7, 50, 8, 2, 7], 216),
    ([3, 8, 6, 1, 3, 50], 708),
    ([8, 10, 4, 9, 6, 2], 664),
    ([7, 50, 8, 9, 5, 8], 704),
    ([7, 100, 8, 6, 10, 9], 250),
    ([75, 25, 2, 1, 4, 3], 762),
    ([8, 3, 3, 50, 6, 9], 788),
    ([6, 7, 10, 4, 5, 5], 771),
    ([50, 75, 100, 8, 1, 3], 335),
    ([25, 7, 75, 5, 6, 5], 197),
    ([10, 2, 4, 50, 25, 8], 710),
    ([9, 7, 6, 8, 2, 25], 514),
    ([2, 1, 4, 10, 6, 75], 283),
    ([3, 10, 100, 9, 1, 7], 386),
    ([4, 1, 50, 10, 75, 3], 566),
    ([50, 75, 100, 2, 2, 7], 607),
    ([6, 75, 3, 100, 4, 9], 440),
    ([2, 2, 6, 10, 25, 50], 534),
    ([10, 7, 9, 4, 6, 6], 794),
    ([2, 8, 3, 8, 25, 6], 928),
    ([9, 8, 7, 6, 9, 2], 482),
    ([8, 1, 6, 8, 7, 4], 698),
    ([5, 6, 75, 4, 6, 10], 794),
    ([2, 100, 2, 4, 8, 5], 643),
    ([1, 100, 3, 2, 25, 10], 890),
    ([6, 10, 100, 50, 10, 75], 342),
    ([4, 8, 75, 3, 2, 3], 821),
    ([4, 3, 25, 7, 6, 3], 631),
    ([9, 1, 7, 1, 25, 50], 876),
    ([1, 5, 25, 3, 10, 9], 683),
    ([50, 5, 3, 5, 7, 2], 894),
    ([50, 6, 1, 5, 8, 3], 953),
    ([5, 10, 8, 4, 1, 10], 676),
]
