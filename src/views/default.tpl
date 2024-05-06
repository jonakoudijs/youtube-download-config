<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark" />
    <link rel="stylesheet" href="static/pico.min.css">
    <title>YouTube Download Channels</title>
  </head>
  <body>
    <main class="container">
      <!-- <h1>YouTube Download Channels</h1> -->
      <nav>
        <ul>
          <li><strong>YouTube Download Channels</strong></li>
        </ul>
      </nav>

      % if add_url:
      <article style="background-color:green;"><u>{{add_url}}</u> toegevoegd!</article>
      % end
      % if error_url:
      <article style="background-color:red;"><u>{{error_url}}</u> toevoegen is misgegaan!</article>
      % end
      % if duplicate_url:
      <article style="background-color:blue;"><u>{{duplicate_url}}</u> is al toegevoegd.</article>
      % end
      <form method="post">
        <fieldset role="group">
          <input name="url" type="url" placeholder="Vul in de YouTube channel URL" />
          <input type="submit" value="Voeg toe" />
        </fieldset>
      </form>

      <hr /><br />

      % for item in subscriptions:
      <article>
        {{item}}
        <!-- <a href="#" style="float:right;text-decoration:none;color:red;">X</a> -->
      </article>
      % end

    </main>
  </body>
</html>