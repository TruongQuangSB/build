/**
 * Remove old snapshot
 *
 * @param repo repository of snapshot
 */
def call(Map args) {
    container('jnlp') {
        sshagent (['projects-storage.eclipse.org-bot-ssh']) {
            sh "snapshots=\$(ssh -o BatchMode=yes genie.set@projects-storage.eclipse.org ls /home/data/httpd/download.eclipse.org/set/snapshots/bin/${args.repo}/feature)"
            sh "readarray -t branches < <(git branch)"
            sh "for i in \$[!branches[@]}; do copy=\$(echo \${branches[\$i]} | sed 's/[ *]\\+//g'; branches[\$i]=\$copy; done"
            sh "for snapshot in \$snapshots; do snapshotName=\$(echo \$snapshot | sed 's/\\///g; if [[ ! \${branches[@]} =~ feature/\${snapshotName} ]] ;" +
                "then" +
                "ssh -o BatchMode=yes genie.set@projects-storage.eclipse.org rm -rf /home/data/httpd/download.eclipse.org/set/snapshots/bin/${args.repo}/\${snapshot};" + 
                "fi"
        }
    }
}