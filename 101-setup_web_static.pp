# Task 2
# comment

$indx = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

$s = "server {
        listen 80 default_server;
        listen [::]:80 default_server;

	location /hbnb {
		alias /data/web_static/current;
	}

        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        add_header X-Served-By ${hostname};
        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /var/www/html;
                internal;
        }
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
}"

exec {'apt-update':
    command => '/usr/bin/env apt-get -y update',
}

-> exec {'mkdir':
  command => 'sudo mkdir -p /data/web_static/shared; sudo mkdir -p /data/web_static/releases/test',
}


-> file {'/data/web_static/releases/test/index.html'
  ensure  => 'file',
  path    => '/data/web_static/releases/test/index.html',
  content => "${indx}",


-> package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

-> file {'/var/www/html/index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => "Holberton School\n",
}

-> file {'custom_404.html':
  ensure  => 'file',
  path    => '/var/www/html/custom_404.html',
  content => "Ceci n'est pas une page\n",
}


-> file {'/etc/nginx/sites-available/default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  content => "${s} ",
}

-> exec {'chown':
  command => 'sudo chown -R ubuntu:ubuntu /data',
}

-> exec {'rm':
  command => 'sudo rm -f /data/web_static/current',
}

-> exec {'ln':
  command => 'sudo ln -s /data/web_static/releases/test data/web_static/current',
}

-> service {'nginx':
  ensure  => 'running',
  restart => 'sudo service nginx restart',
}
