from datetime import date
import random

def midRow(project_id, instance, disk, snapshot):
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
                              border-left: 3px solid #068FFF;
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
                                      <p>{project_id}</p>
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
                              border-left: 3px solid #068FFF;
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
                              border-left: 3px solid #068FFF;
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
                              border-right: 3px solid #068FFF;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              border-left: 3px solid #068FFF;
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

def lastRow(project_id, instance, disk, snapshot):
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
                              border-left: 3px solid #068FFF;
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
                                      <p>{project_id}</p>
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
                              border-left: 3px solid #068FFF;
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
                              border-left: 3px solid #068FFF;
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
                              border-right: 3px solid #068FFF;
                              border-bottom: 0px;
                              padding-left: 2px;
                              padding-right: 2px;
                              border-left: 3px solid #068FFF;
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


def innerHeaderForResourceInfo():
   return f''' 
      <!-- Inner Headers -->
      <tr
        style="text-align: center; font-size: 0.9rem"
      >
        <td style="padding: 6px; font-weight: bold">
          Project Name
        </td>
        <td style="padding: 6px; font-weight: bold">
          Resource Name
        </td>
      </tr>
   '''

def resourceInfo(project_id, resource_name):
   return f'''
      <!-- Resource Info -->
      <tr
        style="text-align: center; font-size: 0.7rem"
      >
        <td style="padding: 10px">
          {project_id}
        </td>
        <td style="padding: 10px">
          {resource_name}
        </td>
      </tr>
   '''

def sort_array_of_dictionaries_by_disk_size(array):
  def _get_size(dictionary):
    return dictionary["disk_size"]
  
  return sorted(array, key=_get_size)

def sort_array_of_dictionaries_by_snapshot_size(array):
  def _get_size(dictionary):
    return dictionary["snapshot_size"]
  
  return sorted(array, key=_get_size)

def sort_array_of_dictionaries_by_vCpu(array):
  def _get_size(dictionary):
    return dictionary["vCpu"]
  
  return sorted(array, key=_get_size)


def resourceInfoNodeGroupList(node_groups):
   node_group_list = innerHeaderForResourceInfo()
   total = len(node_groups)
   minimum = 5 if total > 5 else total
   goTill = minimum

   if total == 0:
      return ["<tr style='text-align: center; font-size: 0.9rem'><td height='40'><b> No Node Group Found </b></td></tr>", 0, 0]

   random.shuffle(node_groups)
   for node_group in node_groups:
      if goTill == 0:
         break
      node_group_list += resourceInfo(node_group["project_name"], node_group["node_group_name"])
      goTill -= 1

   return [node_group_list, minimum, total]

def resourceInfoDiskList(disks):
   disk_list = innerHeaderForResourceInfo()
   total = len(disks)
   minimum = 5 if total > 5 else total
   goTill = minimum

   if total == 0:
      return ["<tr style='text-align: center; font-size: 0.9rem'><td height='40'><b> No Disks Found </b></td></tr>", 0, 0]

   disks = sort_array_of_dictionaries_by_disk_size(disks)
   for disk in disks:
      if goTill == 0:
         break
      disk_list += resourceInfo(disk["project_name"], disk["disk_name"])
      goTill -= 1

   return [disk_list, minimum, total]

def resourceInfoInstanceList(instances):
   instance_list = innerHeaderForResourceInfo()
   total = len(instances)
   minimum = 5 if total > 5 else total
   goTill = minimum

   if total == 0:
      return ["<tr style='text-align: center; font-size: 0.9rem'><td height='40'><b> No Instances Found </b></td></tr>", 0, 0]

   instances = sort_array_of_dictionaries_by_vCpu(instances)
   for instance in instances:
      if goTill == 0:
         break
      instance_list += resourceInfo(instance["project_name"], instance["instance_name"])
      goTill -= 1

   return [instance_list, minimum, total]

def resourceInfoSnapList(snapshots):
   snapshot_list = innerHeaderForResourceInfo()
   total = len(snapshots)
   minimum = 5 if total > 5 else total
   goTill = minimum

   if total == 0:
      return ["<tr style='text-align: center; font-size: 0.9rem'><td height='40'><b> No Snapshots Found </b></td></tr>", 0, 0]

   snapshots = sort_array_of_dictionaries_by_snapshot_size(snapshots)
   for snapshot in snapshots:
      if goTill == 0:
         break;
      snapshot_list += resourceInfo(snapshot["project_name"], snapshot["snapshot_name"])
      goTill -= 1

   return [snapshot_list, minimum, total]



def generateHTML(instances, disks, snapshots, projects, all_actionable_items):
    months = ["JAN", "FEB", "MAR", "APRIL", "MAY", "JUNE", "JULY", "AUG", "SEP", "OCT", "NOV", "DEC"]
    utilization_rows = ""
    proj_len = len(projects)
    today =  date.today()
    
    print("Today's date:", today)
    month = months[int(today.strftime("%m")) - 1]
    year = today.strftime("%Y")

    # Generate utilization rows
    for i in range(proj_len):
        project_id = projects[i]['project_id']
        instance = projects[i]['instances']
        disk = projects[i]['disks']
        snapshot = projects[i]['snapshots']
        
        if (proj_len - 1):
          utilization_rows += lastRow(project_id, instance, disk, snapshot)
        else:
          utilization_rows += midRow(project_id, instance, disk, snapshot)
    
    
    # Get resource info
    resources_node_group_html, minimum_node_groups_count, total_node_groups_count = resourceInfoNodeGroupList(all_actionable_items["nodeGroups"].copy())
    resources_disk_html, minimum_disks_count, total_disks_count = resourceInfoDiskList(all_actionable_items["disks"].copy())
    resources_instance_html, minimum_instances_count, total_instances_count = resourceInfoInstanceList(all_actionable_items["instances"].copy())
    resources_snapshot_html, minimum_snapshots_count, total_snapshots_count = resourceInfoSnapList(all_actionable_items["snapshots"].copy())

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
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
      integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
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

      @font-face {{
        font-family: "Josefin Sans";
        src: url("../fonts/JosefinSans-Bold.ttf") format("truetype");
        font-weight: bold; /* Adjust the weight as needed */
        font-style: normal; /* Adjust the style as needed */
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
                                        font-family: Montserrat, sans-serif;
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
                                        src="https://storage.googleapis.com/gcp-script-bucket/GCPMain.jpg"
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
                        background-color: #e9f0ff;
                        background-position: top center;
                        color: #000000;
                        width: 640px;
                      "
                      width="640"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              padding: 30px 20px 0;
                              text-align: center;
                              font-weight: bold;
                              font-family: 'Josefin Sans', sans-serif;
                              font-size: 2rem;
                              background-color: #222222;
                              color: white;
                            "
                          >
                            Action Items
                          </td>
                        </tr>
                        <tr>
                          <td
                            style="
                              padding: 30px 20px 50px;
                              background-color: #222222;
                              color: white;
                            "
                          >
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
                                background-position: top center;
                                width: 550px;
                                font-family: Montserrat, sans-serif;
                              "
                            >
                              <tbody>
                                <tr style="color: white">
                                  <td
                                    colspan="3"
                                    style="
                                      padding: 10px;
                                      border-bottom: 2px solid white;
                                      font-size: 1.5rem;
                                    "
                                  >
                                    <strong>Alerts</strong>
                                    <img
                                      src="https://cdn-icons-png.flaticon.com/512/4201/4201973.png"
                                      alt="alert"
                                      style="
                                        width: 25px;
                                        vertical-align: bottom;
                                      "
                                    />
                                    <span
                                      style="
                                        font-style: italic;
                                        font-size: 0.8rem;
                                      "
                                      >(Please remove these items)</span
                                    >
                                  </td>
                                </tr>
                                
                                <!-- BREAKER -->
                                <tr>
                                  <td height="30"></td>
                                </tr>

                                <!-- Outer Header Instances -->
                                <tr style="text-align: left; font-size: 1.2rem">
                                  <td
                                    colspan="2"
                                    style="
                                      padding-left: 10px;
                                      font-weight: bold;
                                      font-family: 'Verdana', 'Arial',
                                        sans-serif;
                                      border-bottom: 1px solid white;
                                    "
                                  >
                                    Instances
                                    <span
                                      style="
                                        font-size: 0.6rem;
                                        font-weight: normal;
                                      "
                                      >(Number of vCPU >= 16 | Top {minimum_instances_count} out of {total_instances_count}
                                      | Check the attacment for more info)</span
                                    >
                                  </td>
                                </tr>

                                {resources_instance_html}

                                <!-- BREAKER -->
                                <tr>
                                  <td height="10"></td>
                                </tr>

                                <!-- Outer Header Disks -->
                                <tr style="text-align: left; font-size: 1.2rem">
                                  <td
                                    colspan="2"
                                    style="
                                      font-weight: bold;
                                      font-family: 'Verdana', 'Arial',
                                        sans-serif;
                                      border-bottom: 1px solid white;
                                      padding-left: 10px;
                                    "
                                  >
                                    Disks
                                    <span
                                      style="
                                        font-size: 0.6rem;
                                        font-weight: normal;
                                      "
                                      >(Size More Than 500GB | Top {minimum_disks_count} out of {total_disks_count}
                                      | Check the attacment for more info)</span
                                    >
                                  </td>
                                </tr>

                                {resources_disk_html}


                                <!-- BREAKER -->
                                <tr>
                                  <td height="10"></td>
                                </tr>

                                <!-- Outer Header Snapshots -->
                                <tr style="text-align: left; font-size: 1.2rem">
                                  <td
                                    colspan="2"
                                    style="
                                      font-weight: bold;
                                      font-family: 'Verdana', 'Arial',
                                        sans-serif;
                                      border-bottom: 1px solid white;
                                      padding-left: 10px;
                                    "
                                  >
                                    Snapshots
                                    <span
                                      style="
                                        font-size: 0.6rem;
                                        font-weight: normal;
                                      "
                                      >(Size More Than 200GB | Top {minimum_snapshots_count} out of {total_snapshots_count}
                                      | Check the attacment for more info)</span
                                    >
                                  </td>
                                </tr>

                                {resources_snapshot_html}


                                <!-- BREAKER -->
                                <tr>
                                  <td height="10"></td>
                                </tr>

                                <!-- Outer Header Snapshots -->
                                <tr style="text-align: left; font-size: 1.2rem">
                                  <td
                                    colspan="2"
                                    style="
                                      font-weight: bold;
                                      font-family: 'Verdana', 'Arial',
                                        sans-serif;
                                      border-bottom: 1px solid white;
                                      padding-left: 10px;
                                    "
                                  >
                                    Sole Tenents
                                    <span
                                      style="
                                        font-size: 0.6rem;
                                        font-weight: normal;
                                      "
                                      >(Top {minimum_node_groups_count} out of {total_node_groups_count} | Check the attacment
                                      for more info)</span
                                    >
                                  </td>
                                </tr>

                                {resources_node_group_html}

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
              class="row row-7"
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
              class="row row-8"
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
                              border-top: 3px solid #068FFF;
                              border-right: 0px;
                              border-left: 3px solid #068FFF;
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
                              border-top: 3px solid #068FFF;
                              border-right: 0px;
                              border-left: 3px solid #068FFF;
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
                              border-top: 3px solid #068FFF;
                              border-right: 0px;
                              border-left: 3px solid #068FFF;
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
                              border-top: 3px solid #068FFF;
                              border-right: 3px solid #068FFF;
                              border-left: 3px solid #068FFF;
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

                        {utilization_rows}

                        <tr class="reverse">
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              border-top: 3px solid #068FFF;
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
                              border-top: 3px solid #068FFF;
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
                              border-top: 3px solid #068FFF;
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
                              border-top: 3px solid #068FFF;
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