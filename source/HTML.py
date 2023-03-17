from datetime import date

def midRow(projName, instance, disk, snapshot):
    return f'''
                        <tr>
                          <td height="5"></td>
                        </tr>

                        <tr class="reverse" height="80">
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 3px solid coral;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{projName}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                              border-left: 3px solid coral;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{instance}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                              border-left: 3px solid coral;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{disk}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 3px solid coral;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              border-left: 3px solid coral;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{snapshot}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                        </tr>
    '''

def lastRow(projName, instance, disk, snapshot):
    return f'''
                          <tr class="reverse" height="80">
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 3px solid coral;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{projName}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                              border-left: 3px solid coral;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{instance}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                              border-left: 3px solid coral;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{disk}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 0px;
                              border-right: 3px solid coral;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              border-left: 3px solid coral;
                              width: 25%;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Open Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>{snapshot}</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                        </tr>
    '''

def generateHTML(instances, disks, snapshots, projects):
    months = ["JAN", "FEB", "MAR", "APRIL", "MAY", "JUNE", "JULY", "AUG", "SEP", "OCT", "NOV", "DEC"]
    utilizationRows = ""
    projLen = len(projects)
    today =  date.today()
    
    print("Today's date:", today)
    month = months[int(today.strftime("%m")) - 1]
    year = today.strftime("%Y")

    for i in range(projLen):
        projName = projects[i]['projectName']
        instance = projects[i]['instances']
        disk = projects[i]['disks']
        snapshot = projects[i]['snapshots']
        
        if (projLen - 1):
          utilizationRows += lastRow(projName, instance, disk, snapshot)
        else:
          utilizationRows += midRow(projName, instance, disk, snapshot)
    
    

    return f"""
<!DOCTYPE html>
<html
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  lang="en"
>
  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet"
    />
    <!--[if mso
      ]><xml
        ><o:OfficeDocumentSettings
          ><o:PixelsPerInch>96</o:PixelsPerInch
          ><o:AllowPNG /></o:OfficeDocumentSettings></xml
    ><![endif]-->
    <!--[if !mso]><!-->
    <link
      href="https://fonts.googleapis.com/css?family=Montserrat"
      rel="stylesheet"
      type="text/css"
    />
    <!--<![endif]-->
    <style>
      * {{
        box-sizing: border-box;
      }}

      body {{
        margin: 0;
        padding: 0;
        font-family: "Open Sans", sans-serif;
      }}

      a[x-apple-data-detectors] {{
        color: inherit !important;
        text-decoration: inherit !important;
      }}

      #MessageViewBody a {{
        color: inherit;
        text-decoration: none;
      }}

      p {{
        line-height: inherit;
      }}

      .desktop_hide,
      .desktop_hide table {{
        mso-hide: all;
        display: none;
        max-height: 0px;
        overflow: hidden;
      }}

      .menu_block.desktop_hide .menu-links span {{
        mso-hide: all;
      }}

      @media (max-width: 660px) {{
        .desktop_hide table.icons-inner,
        .social_block.desktop_hide .social-table {{
          display: inline-block !important;
        }}

        .icons-inner {{
          text-align: center;
        }}

        .icons-inner td {{
          margin: 0 auto;
        }}

        .fullMobileWidth,
        .image_block img.big,
        .row-content {{
          width: 100% !important;
        }}

        .mobile_hide {{
          display: none;
        }}

        .stack .column {{
          width: 100%;
          display: block;
        }}

        .mobile_hide {{
          min-height: 0;
          max-height: 0;
          max-width: 0;
          overflow: hidden;
          font-size: 0px;
        }}

        .desktop_hide,
        .desktop_hide table {{
          display: table !important;
          max-height: none !important;
        }}

        .reverse {{
          display: table;
          width: 100%;
        }}

        .reverse .column.first {{
          display: table-footer-group !important;
        }}

        .reverse .column.last {{
          display: table-header-group !important;
        }}

        .row-10 td.column.first .border,
        .row-10 td.column.last .border,
        .row-12 td.column.first .border,
        .row-12 td.column.last .border,
        .row-2 td.column.first .border,
        .row-21 td.column.first .border,
        .row-21 td.column.last .border {{
          padding-left: 25px;
          padding-right: 25px;
          border-top: 0;
          border-right: 0px;
          border-bottom: 0;
          border-left: 0;
        }}

        .row-2 td.column.last .border {{
          padding-left: 0;
          padding-right: 0;
          border-top: 0;
          border-right: 0px;
          border-bottom: 0;
          border-left: 0;
        }}
      }}
    </style>
  </head>

  <body
    style="
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: none;
      text-size-adjust: none;
    "
  >
    <table
      class="nl-container"
      width="100%"
      border="0"
      cellpadding="0"
      cellspacing="0"
      role="presentation"
      style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
    >
      <tbody>
        <tr>
          <td>
            <table
              class="row row-1"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        color: #000000;
                        width: 640px;
                        background-color: #4285f4;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="image_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-bottom: 25px;
                                    width: 100%;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                    padding-top: 25px;
                                  "
                                >
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="
                                      color: #fff;
                                      font-family: 'Josefin Sans', sans-serif;
                                    "
                                  >
                                    <h1>GCP WEEKLY USAGE REPORT</h1>
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-2"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #e9f0ff;
                        background-position: top center;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr class="reverse">
                          <td
                            class="column column-1 first"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div class="border">
                              <table
                                class="heading_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="text-align: center; width: 100%"
                                  >
                                    <h1
                                      style="
                                        margin: 0;
                                        color: #4285f4;
                                        direction: ltr;
                                        font-size: 100px;
                                        font-weight: 400;
                                        letter-spacing: 4px;
                                        text-align: center;
                                        margin-top: 0;
                                        margin-bottom: 0;
                                      "
                                    >
                                      <strong>{month} {year}</strong>
                                    </h1>
                                  </td>
                                </tr>
                              </table>
                              <table
                                class="text_block block-3"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  word-break: break-word;
                                "
                              ></table>
                            </div>
                          </td>
                          <td
                            class="column column-2 last"
                            width="50%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <img
                                        src="https://www.seekpng.com/png/detail/357-3579815_google-cloud-platform-governors-institute-of-vermont.png"
                                        style="
                                          display: block;
                                          border: 0;
                                          width: 320px;
                                          max-width: 100%;
                                        "
                                        width="320"
                                        alt="carousel"
                                        title="carousel"
                                      />
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-3"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #ffffff;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              padding-top: 60px;
                              padding-bottom: 45px;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="heading_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="text-align: center; width: 100%"
                                >
                                  <h2
                                    style="
                                      margin: 0;
                                      color: #1b1b1b;
                                      direction: ltr;
                                      font-size: 38px;
                                      font-weight: bold;
                                      letter-spacing: normal;
                                      line-height: 120%;
                                      text-align: center;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    Total Resources This Week
                                  </h2>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-4"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #ffffff;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="33.333333333333336%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="text_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 10px">
                                  <div
                                    style="font-family: 'Open Sans', sans-serif"
                                  >
                                    <div
                                      class
                                      style="
                                        font-size: 14px;
                                        mso-line-height-alt: 16.8px;
                                        color: #0f9d58;
                                        line-height: 1.2;
                                      "
                                    >
                                      <p
                                        style="
                                          margin: 0;
                                          font-size: 14px;
                                          text-align: center;
                                          mso-line-height-alt: 16.8px;
                                        "
                                      >
                                        <strong
                                          ><span style="font-size: 22px"
                                            >Instances</span
                                          ></strong
                                        >
                                      </p>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="image_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    width: 100%;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <img
                                      src="https://symbols.getvecta.com/stencil_4/53_google-compute-engine.e3f3860416.svg"
                                      style="
                                        display: block;
                                        height: auto;
                                        border: 0;
                                        width: 163px;
                                        max-width: 100%;
                                      "
                                      width="163"
                                      alt="Compute Engine"
                                      title="Compute Engine"
                                    />
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="text_block block-4"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-top: 15px;
                                    padding-bottom: 25px;
                                  "
                                >
                                  <div
                                    style="font-family: 'Open Sans', sans-serif"
                                  >
                                    <div
                                      class
                                      style="
                                        font-size: 14px;
                                        mso-line-height-alt: 16.8px;
                                        color: #1b1b1b;
                                        line-height: 1.2;
                                      "
                                    >
                                      <p
                                        style="
                                          margin: 0;
                                          font-size: 14px;
                                          font-weight: bold;
                                          text-align: center;
                                          mso-line-height-alt: 16.8px;
                                        "
                                      >
                                        <span style="font-size: 16px">{instances}</span>
                                      </p>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                          <td
                            class="column column-2"
                            width="33.333333333333336%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="text_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 10px">
                                  <div
                                    style="font-family: 'Open Sans', sans-serif"
                                  >
                                    <div
                                      class
                                      style="
                                        font-size: 14px;
                                        mso-line-height-alt: 16.8px;
                                        color: #f4b400;
                                        line-height: 1.2;
                                      "
                                    >
                                      <p
                                        style="
                                          margin: 0;
                                          font-size: 14px;
                                          text-align: center;
                                          mso-line-height-alt: 16.8px;
                                        "
                                      >
                                        <strong
                                          ><span style="font-size: 22px"
                                            >Disks</span
                                          ></strong
                                        >
                                      </p>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="image_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    width: 100%;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <img
                                      src="https://symbols.getvecta.com/stencil_4/47_google-cloud-storage.fee263d33a.svg"
                                      style="
                                        display: block;
                                        border: 0;
                                        width: 163px;
                                        height: auto;
                                      "
                                      width="163"
                                      alt="marker"
                                      title="marker"
                                    />
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="text_block block-4"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-top: 15px;
                                    padding-bottom: 25px;
                                  "
                                >
                                  <div
                                    style="font-family: 'Open Sans', sans-serif"
                                  >
                                    <div
                                      class
                                      style="
                                        font-size: 14px;
                                        mso-line-height-alt: 16.8px;
                                        color: #1b1b1b;
                                        line-height: 1.2;
                                      "
                                    >
                                      <p
                                        style="
                                          margin: 0;
                                          font-size: 14px;
                                          text-align: center;
                                          mso-line-height-alt: 16.8px;
                                          font-weight: bold;
                                        "
                                      >
                                        <span style="font-size: 16px">{disks}</span>
                                      </p>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                          <td
                            class="column column-3"
                            width="33.333333333333336%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="text_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td class="pad" style="padding-bottom: 10px">
                                  <div
                                    style="font-family: 'Open Sans', sans-serif"
                                  >
                                    <div
                                      class
                                      style="
                                        font-size: 14px;
                                        mso-line-height-alt: 16.8px;
                                        color: #db4437;
                                        line-height: 1.2;
                                      "
                                    >
                                      <p
                                        style="
                                          margin: 0;
                                          font-size: 14px;
                                          text-align: center;
                                          mso-line-height-alt: 16.8px;
                                        "
                                      >
                                        <strong
                                          ><span style="font-size: 22px"
                                            >Snapshots</span
                                          ></strong
                                        >
                                      </p>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="image_block block-3"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    width: 100%;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div
                                    class="alignment"
                                    align="center"
                                    style="line-height: 10px"
                                  >
                                    <img
                                      src="https://symbols.getvecta.com/stencil_4/18_google-cloud-datastore.aa08661021.svg"
                                      style="
                                        display: block;
                                        height: auto;
                                        border: 0;
                                        width: 163px;
                                        max-width: 100%;
                                      "
                                      width="163"
                                      alt="marker"
                                      title="marker"
                                    />
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <table
                              class="text_block block-4"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                word-break: break-word;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    padding-top: 15px;
                                    padding-bottom: 25px;
                                  "
                                >
                                  <div
                                    style="font-family: 'Open Sans', sans-serif"
                                  >
                                    <div
                                      class
                                      style="
                                        font-size: 14px;
                                        mso-line-height-alt: 16.8px;
                                        color: #1b1b1b;
                                        line-height: 1.2;
                                      "
                                    >
                                      <p
                                        style="
                                          margin: 0;
                                          font-size: 14px;
                                          text-align: center;
                                          mso-line-height-alt: 16.8px;
                                          font-weight: bold;
                                        "
                                      >
                                        <span style="font-size: 16px">{snapshots}</span>
                                      </p>
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              class="row row-5"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #ffffff;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: top;
                              padding-top: 0px;
                              padding-bottom: 0px;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div
                              class="spacer_block"
                              style="
                                height: 60px;
                                line-height: 60px;
                                font-size: 1px;
                              "
                            >
                              &#8202;
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              class="row row-6"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #4285f4;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: top;
                              padding-top: 0px;
                              padding-bottom: 0px;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div
                              class="spacer_block"
                              style="
                                height: 40px;
                                line-height: 40px;
                                font-size: 1px;
                              "
                            >
                              &#8202;
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              class="row row-9"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #e9f0ff;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-left: 25px;
                              padding-right: 25px;
                              vertical-align: top;
                              padding-top: 60px;
                              padding-bottom: 35px;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <table
                              class="heading_block block-2"
                              width="100%"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="text-align: center; width: 100%"
                                >
                                  <h2
                                    style="
                                      margin: 0;
                                      color: #1b1b1b;
                                      direction: ltr;
                                      font-size: 38px;
                                      font-weight: bold;
                                      font-weight: bold;
                                      letter-spacing: normal;
                                      line-height: 120%;
                                      text-align: center;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    Project Vise Utilization
                                  </h2>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              class="row row-10"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #e9f0ff;
                        color: #000000;
                        padding-left: 25px !important;
                        padding-right: 25px !important;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr class="reverse" height="50">
                          <td
                            class="column column-1"
                            width="25%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 3px solid green;
                              border-right: 0px;
                              border-left: 3px solid green;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Josefin Sans', sans-serif;
                                      font-weight: bold;
                                      font-size: 20px;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>Project Name</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            width="25%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 3px solid green;
                              border-right: 0px;
                              border-left: 3px solid green;
                              padding-left: 2px;
                              padding-right: 2px;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-weight: bold;
                                      font-size: 20px;
                                      font-family: 'Josefin Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>Instances</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            width="25%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 3px solid green;
                              border-right: 0px;
                              border-left: 3px solid green;
                              padding-left: 2px;
                              padding-right: 2px;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-weight: bold;
                                      font-size: 20px;
                                      font-family: 'Josefin Sans', sans-serif;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>Disks</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                          <td
                            class="column column-1"
                            width="25%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: center;
                              border-top: 3px solid green;
                              border-right: 3px solid green;
                              border-left: 3px solid green;
                            "
                          >
                            <div class="border">
                              <table
                                class="image_block block-2"
                                width="100%"
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                "
                              >
                                <tr>
                                  <td
                                    class="pad"
                                    style="
                                      width: 100%;
                                      padding-right: 0px;
                                      padding-left: 0px;
                                      font-family: 'Josefin Sans', sans-serif;
                                      font-size: 20px;
                                      font-weight: bold;
                                    "
                                  >
                                    <div class="alignment" align="center">
                                      <p>Snapshots</p>
                                    </div>
                                  </td>
                                </tr>
                              </table>
                            </div>
                          </td>
                        </tr>

                        {utilizationRows}

                        <tr class="reverse">
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              border-top: 3px solid coral;
                              vertical-align: center;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          ></td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              border-top: 3px solid coral;
                              vertical-align: center;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          ></td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              border-top: 3px solid coral;
                              vertical-align: center;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          ></td>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              border-top: 3px solid coral;
                              vertical-align: center;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              width: 25%;
                            "
                          ></td>
                        </tr>

                        <tr class="reverse" height="100"></tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              class="row row-6"
              align="center"
              width="100%"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      class="row-content stack"
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #4285f4;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            width="100%"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: top;
                              padding-top: 0px;
                              padding-bottom: 0px;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                          >
                            <div
                              class="spacer_block"
                              style="
                                height: 40px;
                                line-height: 40px;
                                font-size: 1px;
                              "
                            >
                              &#8202;
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- End -->
  </body>
</html>

    """