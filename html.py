from os import write


def stworzRaportHtml():
    data_list = []
    chessboard = []
    chessboard_list = []

    for files_in in range(6):
        f = open(f"./input/file{files_in+1}.txt", "r")
        data_list.append(f.read().split())

    for files_out in range(6):
        try:
            f = open(f"./output/output{files_out+1}.txt", "r")
            for i in f:
                chessboard.append(i.replace("\t\n", "").split("\t"))
            chessboard_list.append(chessboard.copy())
            chessboard.clear()
            f.close()
        except:
            for i in range(8):
                chessboard.append(["", "", "", "", "", "", "", ""])
            chessboard_list.append(chessboard.copy())
            chessboard.clear()

    f = open("./raport/raport.html", "w", encoding="utf8")

    f.write(
        """<html>

<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <title>Raport projektu</title>
    <style>
        html,body{
            margin: 0;
            background-color: #f1f1f1;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            width: 100%;
            height: 100%;
        }
        body{
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        header{
             color: white;
        background-color: #128153;
        margin: 0;
        padding: 15px;
        }
        h1{
            text-align: center;
            margin: 0;
            margin-top: 5px;
            margin-bottom: 5px;
        }
        h5{
            text-align: center;
            margin-top: 5px;
            margin-bottom: 5px;
        }
        .content{
            flex: 1;
            padding: 15px;
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }
        table.mainTable{
            border-collapse: collapse;
            margin: 0 10px;
            width: 40%;
            border-radius: 15px;
            background-color: #dddddd;
            text-align: center;
        }
        .output{
            text-align: center;
        }
        table.mainTable>tbody>tr>th{
            height: 40px;
        }
        table.mainTable>tbody>tr>td{
            padding: 5px;
            background-color: #ececec;
            height: 100%;
            vertical-align: center;
        }
        table.mainTable>tr>td:hover{
            background-color: #def1fd;
        }
        table.mainTable>tbody>tr:nth-child(2n+1)>td{
            background-color: #e4e4e4;
        }
        table.mainTable>tbody>tr:last-child>td:first-child{
            border-bottom-left-radius: 15px;
        }
        table.mainTable>tbody>tr:last-child>td:last-child{
            border-bottom-right-radius: 15px;
        }
        table.chessboard{
            border: solid 1px black;
            border-collapse: collapse;
        }
        table.chessboard td{
            border: solid 1px black;
            width: 35px;
            height: 35px;
            text-align: center;
            vertical-align: center;
        }
        table td.last{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 25px !important;
        }
        footer{
            color: white;
        background-color: #128153;
        padding: 5px;
        }
        footer p {
            text-align: center;
            margin: 2px;
        }
    </style>
</head>

<body>
    <header>
        <h1>SZACHOWNICA</h1>
    </header>
    <div class='content'>
    <table class='mainTable'>
        <tr>
            <th>Input data</th>
            <th></th>
            <th>Output data</th>
        </tr>
        """
    )

    for i in range(0, len(data_list), 1):
        f.write("<tr>\n")
        f.write("<td>\n")
        for j in data_list[i]:
            f.write(str(j) + " ")
        f.write("</td>\n")
        f.write("<td>\n")
        f.write("<i class='fas fa-arrow-right'></i>\n")
        f.write("</td>\n")
        f.write("<td class='last'>\n")
        f.write("<table class='chessboard'>")
        for j in chessboard_list[i]:
            f.write("<tr>")
            for k in j:
                f.write("<td>")
                if str(k) != "--":
                    f.write(str(k))
                f.write("</td>")
            f.write("</tr>")
        f.write("</table>")
        f.write("</td>\n")
        f.write("</tr>\n")

    f.write(
        """
    </table>
    </div>
    <footer>
        <p>
            Dyba Piotr, 2022, Języki Skryptowe - Projekt 1
        </p>
    </footer>
</body>

</html>
        """
    )
    f.close()


stworzRaportHtml()
