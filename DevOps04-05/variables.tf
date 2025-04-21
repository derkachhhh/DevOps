variable "provider_token" {
  description = "dop_v1_12457890abcDef12345670abCdef1267890abcdef1234567890abcdfv"
  type        = string
  sensitive   = true
}

variable "ssh_keys" {
  description = "List of SSH public keys to add to servers"
  type        = list(string)
  default = [
    "SHA256:iTIh4Dmwalq8SQO59V17DrfoBhG8HxGq3G67FBKyL64 derkachelizabeth@gmail.com", 
    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOkAhvfRyUvgsUwENIds1a/4OvuHQgLki8K1EzPltl5M i.ilin@iilin-pro14.local"        
  ]
}

variable "server_count" {
  description = "Number of servers to create"
  type        = number
  default     = 2
}

variable "server_size" {
  description = "Server size specification"
  type        = string
  default     = "s-2vcpu-4gb" # 2 CPU, 4GB RAM
}

variable "region" {
  description = "Cloud provider region"
  type        = string
  default     = "fra1" # Frankfurt
}

variable "postgres_ports" {
  description = "PostgreSQL ports to open between servers"
  type        = list(number)
  default     = [5432, 5433, 5434, 5435]
}